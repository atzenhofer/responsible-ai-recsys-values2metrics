# Toy Example Calculations

Python implementation of metric calculations from the paper's illustrative example. It demonstrates that the proposed metrics are computable and discriminate between recommendation strategies.

## Files

**Core Implementation** (`src/`):
- `data.py` - Fixed toy data (R1, R2) and system parameters
- `metrics.py` - Metric implementations (RPQ, CR, CA, MWR, DRI, CSVA)
- `config.py` - Stakeholder weight configurations

**Scripts**:
- `main.py` - Reproduces metric values from the paper
- `simulation.py` - Robustness testing with random trials
- `weight_sensitivity.py` - Weight sensitivity analysis

## Usage

**Requirements**: Python 3.8+ and numpy

```bash
pip install numpy
python3 main.py
```

This outputs individual metric values and CSVA scores matching the paper's illustrative example.

## Optional Analyses

```bash
python3 simulation.py         # 100 random trials
python3 weight_sensitivity.py # ±10% weight variations
```
