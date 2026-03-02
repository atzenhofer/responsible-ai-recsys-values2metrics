# Toy Example Calculations

Python implementation of metric calculations from the paper's illustrative example. Three systems are evaluated: R1 (popularity-based), R2 (balanced multistakeholder), R3 (relevance-optimized). The script reproduces the individual metric table and CSVA scenario table (z-score normalization, three weighting schemes) reported in the paper. The paper's illustrative example section documents the instantiation used here.

## Files

**Core Implementation** (`src/`):
- `data.py` - Fixed toy data (R1, R2, R3) and system parameters
- `metrics.py` - Metric implementations (RPQ, CR, CA, MWR, DRI, CSVA, normalization)
- `config.py` - Stakeholder weight configurations

**Scripts**:
- `main.py` - Reproduces metric values and CSVA scores from the paper
- `simulation.py` - Robustness testing with random trials
- `weight_sensitivity.py` - Weight sensitivity analysis

## Usage

**Requirements**: Python 3.8+ and numpy
```bash
python main.py # Main program
```


Output: individual metrics (RPQ, CR, CA, MWR, DRI) for R1, R2, R3 and CSVA scores for Consumer, Provider, and Balanced scenarios.

## Metric Directions

All metrics are oriented so that higher is better: RPQ (novelty), CR (fairness), CA (context match), MWR (metadata-weighted relevance), DRI (thematic coherence). CSVA aggregates these via weighted sum.

## Adapting sim() for Other Domains

DRI uses `sim(i,j) = 1 - |sem_i - sem_j|` as a scalar proxy for item similarity. For other domains, this might be replaced with an appropriate similarity function (e.g., cosine similarity over embeddings, Jaccard over tags). The paper describes this as a "task-conditioned utility signal."

## Simulation profiles (`simulation.py`)

The simulation draws random lists with three profiles that mirror R1/R2/R3: **popularity** (high raters, A-heavy archives, sorted by popularity --> low RPQ/CR/CA); **balanced** (mid raters, even archives, sem near user profile --> high RPQ/CR/CA); **relevance** (mid–high raters, A-heavy, tight sem and high meta --> high MWR/DRI). All items have `rel=1` (no irrelevance); the script checks that metric ordering by profile is plausible, not exact paper numbers.

## Optional Analyses

```bash
python simulation.py         # 100 random trials
python weight_sensitivity.py # ±10% weight variations
```
