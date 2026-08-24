from benchmark import make
from chameleon import ChameleonEvaluator, Behavior

def collapse_contexts(data):
    all_reps = []
    for reps in data.values():
        all_reps.extend(reps)
    return {"all": all_reps}

if __name__ == "__main__":
    data = make()
    full = ChameleonEvaluator().evaluate_task(data)
    ablated = ChameleonEvaluator().evaluate_task(collapse_contexts(data))
    print("full context sensitivity:", full["context_sensitivity"])
    print("collapsed context sensitivity:", ablated["context_sensitivity"])
