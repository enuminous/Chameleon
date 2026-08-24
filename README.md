# CHAMELEON — EFMW Zoo #27

**Contextual Habitat Adaptation and Model Evaluation under Latent Environmental Observation Noise**

CHAMELEON is an experimental EFMW-inspired framework for detecting when a system's behavior changes materially across contexts, interfaces, evaluators, environments, or observation conditions.

## Core question

> Is the system actually stable, or does it present different behavior depending on where, how, and by whom it is observed?

CHAMELEON separates legitimate adaptation from concerning context dependence.

## Primary outputs

- context sensitivity
- behavior divergence
- evaluator sensitivity
- interface sensitivity
- latent-noise robustness
- adaptation consistency
- hidden regime-change score

## Repository contents

- `theory.md`
- `architecture.md`
- `context_model.md`
- `limitations.md`
- `chameleon.py`
- `benchmark.py`
- `ablations.py`
- `test_chameleon.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_chameleon.py
```

## Zoo position

MAGPIE #24 tracks grounding.

WOLF #25 tracks weak distributed failure precursors.

ELEPHANT #26 tracks historical continuity.

**CHAMELEON #27 asks whether the system remains behaviorally coherent when its habitat changes.**
