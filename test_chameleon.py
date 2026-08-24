import unittest
from chameleon import ChameleonEvaluator, Behavior

class TestChameleon(unittest.TestCase):
    def test_identical_contexts_low_divergence(self):
        obs = {
            "a":[Behavior({"x":1.0}),Behavior({"x":1.0})],
            "b":[Behavior({"x":1.0}),Behavior({"x":1.0})],
        }
        out = ChameleonEvaluator().evaluate_task(obs)
        self.assertAlmostEqual(out["context_sensitivity"], 0.0)

    def test_shift_detected(self):
        obs = {
            "a":[Behavior({"x":0.0}),Behavior({"x":0.0})],
            "b":[Behavior({"x":1.0}),Behavior({"x":1.0})],
        }
        out = ChameleonEvaluator().evaluate_task(obs)
        self.assertGreater(out["context_sensitivity"], 0.5)

    def test_expected_adaptation_reduces_unexplained(self):
        obs = {
            "a":[Behavior({"x":0.0})],
            "b":[Behavior({"x":0.4})],
        }
        out = ChameleonEvaluator({("a","b"):0.3}).evaluate_task(obs)
        self.assertLess(out["unexplained"][("a","b")], out["pairwise"][("a","b")])

if __name__ == "__main__":
    unittest.main()
