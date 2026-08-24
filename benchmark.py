import random
from chameleon import ChameleonEvaluator, Behavior

def make(seed=27):
    rng = random.Random(seed)
    data = {}
    for context, shift in [("chat",0.0),("api",0.15),("eval",0.35)]:
        reps = []
        for _ in range(20):
            reps.append(Behavior({
                "accuracy": 0.90 - shift*0.2 + rng.gauss(0,0.015),
                "confidence": 0.75 + shift + rng.gauss(0,0.02),
                "latency_norm": 0.40 + shift*0.3 + rng.gauss(0,0.02),
            }))
        data[context] = reps
    return data

if __name__ == "__main__":
    ev = ChameleonEvaluator()
    result = ev.evaluate_task(make())
    for k,v in result.items():
        print(k, v)
