# Supplementary Materials: From Stakeholder Values to Evaluation Metrics

This repository contains supplementary materials for the paper:

**From Stakeholder Values to Evaluation Metrics: A Co-Design Methodology for Responsible Recommender Systems in Digital Archives**

*Under review*

## Related Work

- [multistakeholder-archives-recsys](https://github.com/atzenhofer/multistakeholder-archives-recsys) — RecSys 2025 short paper on multistakeholder value identification in digital archives

## Repository Contents

This repository includes interview materials from multistakeholder focus groups and computational artifacts demonstrating the proposed metrics. All materials have been carefully anonymized to protect participant privacy.

### Interview Materials

- **[`appendix-stakeholders.md`](appendix-stakeholders.md)**: Anonymized profiles of 25 domain experts across five stakeholder groups
- **[`appendix-focus-groups.md`](appendix-focus-groups.md)**: Focus group methodology and session structure
- **[`appendix-presentation.md`](appendix-presentation.md)**: Discussion scenarios, questions, and provocative statements
- **[`appendix-q&a.md`](appendix-q&a.md)**: Background materials and value framework shared with participants
- **[`appendix-consent-form.md`](appendix-consent-form.md)**: Consent procedures and data protection information (GDPR-compliant)

Full transcripts cannot be shared due to privacy commitments.

### Computational Artifacts

- **[`toy-example-calculations/`](toy-example-calculations/)**: Python implementation of all metrics from the paper's illustrative example. Three recommendation systems (R1: popularity-based, R2: balanced multistakeholder, R3: relevance-optimized) are evaluated; the script reproduces the individual metric values and CSVA scores reported in the paper. See the [toy example README](toy-example-calculations/README.md) for usage details.

## Study Overview

We conducted structured focus groups with 25 domain experts across five stakeholder groups to understand how diverse values might inform recommender system evaluation in digital archives:

| Group | Role Examples |
|-------|--------------|
| **Upstream** (U1-U5) | Archive directors, curators, librarians |
| **Provider** (P1-P5) | Technical managers, archival specialists, data integration specialists |
| **System** (S1-S5) | Developers, system directors, information retrieval specialists |
| **Consumer** (C1-C5) | Senior researchers, doctoral researchers, educators |
| **Downstream** (D1-D5) | Professors, project editors, platform coordinators |

**Sessions**: Five 60-minute structured focus groups with scenario-based discussions on visibility, adaptation, and transparency.

**Value Framework**: Five categories (functional, user experience, responsibility, human/social, technical) shared with participants beforehand.

**Analysis**: Abductive coding approach combining deductive value categories with inductive pattern recognition, revealing tensions and convergences across stakeholder groups.

## Computational Reproducibility

The toy example calculations use fixed data (R1, R2, R3) and deterministic algorithms. Running `python3 main.py` from the `toy-example-calculations/` directory (with dependencies in a venv, e.g. `numpy`) reproduces the individual metric table and CSVA scenario table (z-score normalization, three weighting schemes) reported in the paper.

## License

- Code: MIT
- Research materials/data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Contact

For questions about this research, please contact the corresponding author (florian.atzenhofer-baumgartner@student.tugraz.at).
