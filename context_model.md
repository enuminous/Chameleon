# Context Model

## Context schema

```json
{
  "context_id": "c7",
  "interface": "api",
  "evaluator": "blind-rater-2",
  "domain": "finance",
  "tool_access": true,
  "noise_level": 0.2,
  "role": "assistant"
}
```

## Matched-task requirement

Valid CHAMELEON comparisons should preserve the underlying task while varying selected context dimensions.

## Behavior vector

```json
{
  "accuracy": 0.91,
  "confidence": 0.82,
  "latency": 1.4,
  "compliance": 1.0,
  "tool_calls": 2
}
```

## Context matrix

For tasks `x_1...x_m` and contexts `c_1...c_k`, evaluate:

`B[m][k][d]`

where `d` is behavioral dimensionality.

## Context instability

For each task:

`I_x = mean pairwise distance across contexts`

Overall:

`I = mean_x I_x`

## Noise correction

Use repeated trials within each context.

Estimate:
- between-context variance
- within-context variance

A context effect is stronger when:

`Var_between >> Var_within`

## Hidden adaptation

A large context effect with no declared adaptation rationale is a CHAMELEON target.
