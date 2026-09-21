# Dynamic and Static–Dynamic Model Comparisons

[Up one level](../README.md) · [Repository home](../../../README.md)

Read the individual reports below, or return to the [nine-comparison summary](../result-reports/00_summary.md).

## Comparisons

| Comparison | Implementation | Results |
|---|---|---|
| dynamic FEA vs multimodal | [Notebook](dynamic_fea_vs_multimodal_significance_tests.ipynb) | [Report](../result-reports/05_dynamic_fea_vs_multimodal.md) |
| dynamic image vs FEA | [Notebook](dynamic_image_vs_fea_significance_tests.ipynb) | [Report](../result-reports/04_dynamic_image_vs_fea.md) |
| dynamic image vs multimodal | [Notebook](dynamic_image_vs_multimodal_significance_tests.ipynb) | [Report](../result-reports/06_dynamic_image_vs_multimodal.md) |
| static FEA vs dynamic FEA | [Notebook](static_fea_vs_dynamic_fea_significance_tests.ipynb) | [Report](../result-reports/07_static_vs_dynamic_fea.md) |
| static image vs dynamic image | [Notebook](static_image_vs_dynamic_image_significance_tests.ipynb) | [Report](../result-reports/08_static_vs_dynamic_image.md) |
| static multimodal vs dynamic multimodal | [Notebook](static_multimodal_vs_dynamic_multimodal_significance_tests.ipynb) | [Report](../result-reports/09_static_vs_dynamic_multimodal.md) |

## Inputs and regeneration

- [dynamic_test_predictions.csv](dynamic_test_predictions.csv)
- [static_test_predictions.csv](static_test_predictions.csv)

Use [the prediction collector](collect_dynamic_test_predictions.ipynb) only when regenerating the dynamic export from model files. The static export used for Static–Dynamic comparisons is produced in the sibling static-significance-tests directory. Run the test notebooks from this directory using the existing CSVs to regenerate [numeric result tables](statistical_results).

The current dynamic Multimodal export corresponds to the canonical 81.61% intermediate-fusion result. External datasets and trained models are required for collection, not for reading the saved predictions. See the parent README and comparison plan for paired units, multiplicity, and dependence limits.
