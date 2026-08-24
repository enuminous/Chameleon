# CHAMELEON: Contextual Habitat Adaptation and Model Evaluation under Latent Environmental Observation Noise

## Abstract

CHAMELEON is an experimental framework for measuring context-dependent behavioral variation in intelligent systems. It evaluates matched tasks across multiple habitats, including interfaces, evaluators, domains, and tool configurations, while estimating within-context noise and separating expected adaptation from unexplained divergence.

## 1. Motivation

Single-context evaluation can miss deployment-dependent behavior. A model may appear stable in one setting and substantially change confidence, accuracy, tool usage, refusal behavior, or policy adherence in another.

CHAMELEON treats these differences as a measurable relational object.

## 2. Method

For task x and context c:

`b_c(x)`

denotes a behavior vector.

Pairwise context divergence:

`D(c_i,c_j|x) = dist(b_ci,b_cj)`

Expected adaptation is subtracted:

`U = max(0, D-A*)`

Repeated trials estimate within-context noise.

## 3. Primary metrics

- context sensitivity
- noise-adjusted divergence
- signal-to-noise ratio
- unexplained adaptation
- evaluator sensitivity
- interface sensitivity
- regime-shift rate

## 4. Baselines

- stratified metrics
- ANOVA/MANOVA
- mixed-effects models
- domain robustness benchmarks
- distribution-shift testing
- subgroup evaluation

## 5. Ablations

- collapse context labels
- remove noise correction
- remove expected-adaptation model
- use only scalar accuracy
- remove repeated trials
- randomize context labels

## 6. Falsification

If simple stratified or mixed-effects evaluation captures the same phenomena with equal or better predictive utility, CHAMELEON's additional architecture is not justified.

## 7. Claim boundary

CHAMELEON identifies context-conditioned behavior. It does not establish intent, hidden agency, strategic deception, or consciousness.
