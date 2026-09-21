# Static–Dynamic and Multimodal Error Analysis

[Up one level](../README.md) · [Repository home](../../README.md)

This descriptive analysis compares errors across all six settings and examines fusion outcomes within four unimodal correctness groups.

## Read the results

- [Integrated error-analysis report](outputs/error_analysis_report.md).
- [Figures](outputs/figures/): six confusion matrices, Static–Dynamic deltas, overlap summaries, and fusion visualizations.
- [Tables](outputs/tables/): class metrics, sample transitions, and fusion-group breakdowns.
- [Saved validation record](outputs/validation.json).

## Run the analysis

[dynamic_error_analysis.ipynb](dynamic_error_analysis.ipynb) reads the local [static predictions](static_test_predictions.csv) and [dynamic predictions](dynamic_test_predictions.csv). Run from this directory to regenerate outputs; no training is needed.

The source prediction collectors are documented under [significance tests](../significance-tests/README.md). Image and Multimodal use 756 view rows; FEA-only metrics use 378 unique reenactments. FEA predictions are repeated across paired views for cross-modality alignment only.

## Interpretation

This report is descriptive; inferential tests are in the separate significance-test notebooks. The prediction-selection oracle is not a strict fusion ceiling, and both unimodal models being wrong does not by itself establish human ambiguity. For the relationship between human annotation agreement and model errors, see [FEA analysis, notebook 06](../fea_analysis/README.md).
