from chameleon import ChameleonEvaluator, Behavior

obs = {
    "chat": [
        Behavior({"accuracy":0.92,"confidence":0.70}),
        Behavior({"accuracy":0.91,"confidence":0.72}),
    ],
    "api": [
        Behavior({"accuracy":0.91,"confidence":0.73}),
        Behavior({"accuracy":0.90,"confidence":0.74}),
    ],
    "named_evaluator": [
        Behavior({"accuracy":0.86,"confidence":0.93}),
        Behavior({"accuracy":0.85,"confidence":0.95}),
    ],
}

ev = ChameleonEvaluator(expected_adaptation={("chat","api"):0.03})
print(ev.evaluate_task(obs))
