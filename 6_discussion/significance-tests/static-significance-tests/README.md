# Static Model Comparisons

[Up one level](../README.md) · [Repository home](../../../README.md)

Read the individual reports below, or return to the [nine-comparison summary](../result-reports/00_summary.md).

## Comparisons

| Comparison | Implementation | Results |
|---|---|---|
| static FEA vs multimodal | [Notebook](static_fea_vs_multimodal_significance_tests.ipynb) | [Report](../result-reports/02_static_fea_vs_multimodal.md) |
| static image vs FEA | [Notebook](static_image_vs_fea_significance_tests.ipynb) | [Report](../result-reports/01_static_image_vs_fea.md) |
| static image vs multimodal | [Notebook](static_image_vs_multimodal_significance_tests.ipynb) | [Report](../result-reports/03_static_image_vs_multimodal.md) |

## Inputs and regeneration

- [static_test_predictions.csv](static_test_predictions.csv)

Use [the prediction collector](collect_static_test_predictions.ipynb) only when regenerating the static export from model files.  Run the test notebooks from this directory using the existing CSVs to regenerate [numeric result tables](statistical_results).

Use the [static environment instructions](env/README.md) for the saved static-model generation. External datasets and trained models are required for collection, not for reading the saved predictions. See the parent README and comparison plan for paired units, multiplicity, and dependence limits.
