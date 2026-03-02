# Supplementary Materials: From Stakeholder Values to Evaluation Metrics

This repository contains supplementary materials for the paper "From Stakeholder Values to Evaluation Metrics: A Co-Design Methodology for Responsible Recommender Systems in Digital Archives". Personal and institutional identifiers have been removed to protect participant privacy while maintaining methodological transparency.

## Related Work

This repository extends our prior work:
- [multistakeholder-archives-recsys](https://github.com/atzenhofer/multistakeholder-archives-recsys) — RecSys 2025 short paper on multistakeholder value identification in digital archives

## Repository Contents

This repository includes interview materials from multistakeholder focus groups and computational artifacts demonstrating the proposed metrics.

### Interview Materials

- **[`appendix-stakeholders.md`](appendix-stakeholders.md)**: Anonymized profiles of 25 domain experts across five stakeholder groups (upstream, provider, system, consumer, downstream), including roles, expertise, career stage, and region.
- **[`appendix-presentation.md`](appendix-presentation.md)**: Discussion scenarios, questions, and stakeholder-specific provocative statements used in focus groups.
- **[`appendix-q&a.md`](appendix-q&a.md)**: Background materials and five-category value framework/codebook shared with participants prior to sessions.
- **[`appendix-consent-form.md`](appendix-consent-form.md)**: Consent procedures and data protection information template.
- **[`appendix-focus-groups.md`](appendix-focus-groups.md)**: Session structure and methodology overview.

Full transcripts cannot be shared due to privacy commitments.

### Computational Artifacts

- **[`toy-example-calculations/`](toy-example-calculations/)**: Python implementation of all metrics from the paper's illustrative example. Three recommendation systems (R1: popularity-based, R2: balanced multistakeholder, R3: relevance-optimized) are evaluated; the script reproduces the individual metric values and CSVA scores reported in the paper. See the [toy example README](toy-example-calculations/README.md) for usage details.

## Study Overview

We conducted structured focus groups with 25 domain experts across five stakeholder groups to understand how diverse values might inform recommender system evaluation in digital archives:

| Group | Role Examples |
|-------|---------------|
| **Upstream** (U1-U5) | Archive directors, digital curators, library research heads |
| **Provider** (P1-P5) | IT managers, archival specialists, data integration experts |
| **System** (S1-S5) | Core developers, system directors, information retrieval specialists |
| **Consumer** (C1-C5) | Senior researchers, doctoral students, educators |
| **Downstream** (D1-D5) | History professors, project editors, platform coordinators |

**Sessions**: Five 60-minute structured focus groups with scenario-based discussions on visibility, adaptation, and transparency.

**Value Framework**: Five categories (functional, user experience, responsibility, human/social, technical) shared with participants beforehand.

**Analysis**: Abductive coding approach combining deductive value categories with inductive pattern recognition, revealing tensions and convergences across stakeholder groups.

## Additional Information

**Computational Reproducibility**: The toy example calculations use fixed data (R1, R2, R3) and deterministic algorithms. Running `python3 main.py` from the `toy-example-calculations/` directory (with dependencies in a venv, e.g. `numpy`) reproduces the individual metric table and CSVA scenario table (z-score normalization, three weighting schemes) reported in the paper. The paper's example section documents the instantiation used in the code.

**Limitations**: This repository provides methodological transparency for the focus group study. Full interview transcripts cannot be shared to protect participant privacy as agreed in the consent process.

## License

- Code: MIT
- Research materials/data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Contact

For questions about this research, please contact the corresponding author (florian.atzenhofer-baumgartner@student.tugraz.at).
