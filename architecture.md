# CHAMELEON Architecture

## Pipeline

1. Task Matcher
2. Context Encoder
3. Behavior Vectorizer
4. Noise Estimator
5. Pairwise Divergence Engine
6. Expected-Adaptation Model
7. Regime-Shift Detector
8. Context Attribution Layer
9. Audit Report Generator

## Inputs

- repeated tasks
- controlled context variants
- behavior measurements
- optional expected-adaptation rules
- uncertainty/noise metadata

## Outputs

```json
{
  "context_sensitivity": 0.31,
  "noise_adjusted_divergence": 0.24,
  "evaluator_sensitivity": 0.08,
  "interface_sensitivity": 0.19,
  "regime_shift": false,
  "top_context_pair": ["api", "chat"]
}
```

## Design principle

CHAMELEON should never label all adaptation as instability.

The key distinction is:

**expected adaptation versus unexplained context dependence.**

## Integration

ELEPHANT can preserve longitudinal context history.

MAGPIE can audit the evidence behind claims of context dependence.

WOLF can use CHAMELEON outputs to detect habitat-specific degradation precursors.
