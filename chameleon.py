from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
import math
from statistics import mean, variance

@dataclass
class Behavior:
    values: Dict[str, float]

def euclidean(a: Dict[str,float], b: Dict[str,float]) -> float:
    keys = sorted(set(a) & set(b))
    if not keys:
        return 0.0
    return math.sqrt(sum((a[k]-b[k])**2 for k in keys) / len(keys))

class ChameleonEvaluator:
    def __init__(self, expected_adaptation: Optional[Dict[Tuple[str,str], float]] = None):
        self.expected_adaptation = expected_adaptation or {}

    def evaluate_task(self, observations: Dict[str, List[Behavior]]):
        contexts = list(observations)
        centroids = {}
        within = {}

        for c, reps in observations.items():
            keys = sorted(reps[0].values.keys())
            centroids[c] = {
                k: mean([r.values[k] for r in reps]) for k in keys
            }
            dists = [euclidean(r.values, centroids[c]) for r in reps]
            within[c] = mean(dists) if dists else 0.0

        pairwise = {}
        unexplained = {}
        for i in range(len(contexts)):
            for j in range(i+1, len(contexts)):
                a, b = contexts[i], contexts[j]
                d = euclidean(centroids[a], centroids[b])
                pairwise[(a,b)] = d
                exp = self.expected_adaptation.get((a,b),
                      self.expected_adaptation.get((b,a), 0.0))
                unexplained[(a,b)] = max(0.0, d-exp)

        between = mean(pairwise.values()) if pairwise else 0.0
        noise = mean(within.values()) if within else 0.0
        noise_adjusted = max(0.0, between-noise)
        snr = between/(noise+1e-9) if noise > 0 else (float("inf") if between > 0 else 0.0)

        return {
            "context_sensitivity": between,
            "within_context_noise": noise,
            "noise_adjusted_divergence": noise_adjusted,
            "signal_to_noise": snr,
            "pairwise": pairwise,
            "unexplained": unexplained,
            "centroids": centroids,
        }
