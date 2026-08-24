# CHAMELEON Theory

## 1. Problem

A system may appear stable in one environment and behave differently in another.

Relevant habitat changes include:
- prompt/interface changes,
- evaluator identity,
- role assignment,
- data source changes,
- noise levels,
- observation delay,
- tool availability,
- deployment domain.

CHAMELEON treats context as an explicit variable.

## 2. Context-conditioned behavior

Let:

`y = f(x, c, n)`

where:
- `x` = task/input
- `c` = context/habitat
- `n` = latent observation noise

The goal is not to eliminate adaptation. It is to identify unexplained or harmful divergence across `c`.

## 3. Behavioral representation

For matched task `x`, measure behavior vector:

`b_c(x)`

Possible dimensions:
- action choice,
- confidence,
- latency,
- refusal/compliance,
- tool use,
- factuality,
- policy adherence,
- explanation style,
- error rate.

## 4. Context divergence

For two contexts `c_i, c_j`:

`D(c_i,c_j|x) = dist(b_ci(x), b_cj(x))`

Aggregate:

`CSD = mean_x mean_{i<j} D(c_i,c_j|x)`

## 5. Expected adaptation model

Not all divergence is bad.

Define expected adaptation:

`A*(c_i,c_j|x)`

Then unexplained divergence is:

`U = max(0, D - A*)`

This is the core CHAMELEON distinction.

## 6. Latent observation noise

Observed behavior:

`b_obs = b_true + epsilon`

CHAMELEON should estimate whether context effects remain after accounting for observation noise.

A simple signal-to-noise ratio:

`SNR_c = Var_context / (Var_noise + eps)`

## 7. Evaluator sensitivity

Let evaluator identity be one context dimension.

`E_sens = Var_evaluator(b)`

A system that changes substantially based only on evaluator identity may require deeper examination.

## 8. Regime shifts

For ordered context changes, monitor:

`Delta_t = dist(b_t, b_{t-1})`

A hidden regime shift is candidate-signaled when:

`Delta_t > theta_delta`

while measured task difficulty and explicit environment change remain small.

## 9. EFMW interpretation

The EFMW-inspired element is relational comparison across habitat layers rather than isolated evaluation.

The framework preserves:
- task identity,
- context identity,
- observation uncertainty,
- behavioral trajectory.

## 10. Falsifiable prediction

CHAMELEON should add value when:
- evaluation contexts vary,
- systems adapt conditionally,
- observation noise is nontrivial,
- behavior is stable on surface metrics but unstable relationally.

If ordinary stratified evaluation captures the same effects, the extra framework is unnecessary.
