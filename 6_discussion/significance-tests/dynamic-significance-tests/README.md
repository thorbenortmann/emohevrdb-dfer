# Dynamic and Static–Dynamic Model Comparisons

[Up one level](../README.md) · [Repository README](../../../README.md)

These notebooks use the shared prediction CSVs documented in the [parent README](../README.md#shared-inputs-and-regeneration). Methods, execution instructions, and inference scope are documented there.

| Comparison | Implementation | Saved results | Paper |
| --- | --- | --- | --- |
| Dynamic Image vs. Dynamic FEA | [Notebook](dynamic_image_vs_fea_significance_tests.ipynb) | [Report](../result-reports/04_dynamic_image_vs_fea.md) | Additional |
| Dynamic FEA vs. Dynamic Multimodal | [Notebook](dynamic_fea_vs_multimodal_significance_tests.ipynb) | [Report](../result-reports/05_dynamic_fea_vs_multimodal.md) | Table 7 |
| Dynamic Image vs. Dynamic Multimodal | [Notebook](dynamic_image_vs_multimodal_significance_tests.ipynb) | [Report](../result-reports/06_dynamic_image_vs_multimodal.md) | Table 7 |
| Static FEA vs. Dynamic FEA | [Notebook](static_fea_vs_dynamic_fea_significance_tests.ipynb) | [Report](../result-reports/07_static_vs_dynamic_fea.md) | Table 7 |
| Static Image vs. Dynamic Image | [Notebook](static_image_vs_dynamic_image_significance_tests.ipynb) | [Report](../result-reports/08_static_vs_dynamic_image.md) | Table 7 |
| Static Multimodal vs. Dynamic Multimodal | [Notebook](static_multimodal_vs_dynamic_multimodal_significance_tests.ipynb) | [Report](../result-reports/09_static_vs_dynamic_multimodal.md) | Table 7 |

Run the relevant comparison notebook to regenerate its numerical exports in [statistical_results/](statistical_results/). The exported tables include the primary result, paired reenactment data, sensitivity test, participant summaries, and secondary tests where applicable.

The [combined summary](../result-reports/00_summary.md) collects all nine repository comparisons.
