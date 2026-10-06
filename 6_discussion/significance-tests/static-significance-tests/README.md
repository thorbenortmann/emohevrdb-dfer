# Static Model Comparisons

[Up one level](../README.md) · [Repository README](../../../README.md)

These notebooks use the shared prediction CSVs documented in the [parent README](../README.md#shared-inputs-and-regeneration). Methods, execution instructions, and inference scope are documented there.

| Comparison | Implementation | Saved results | Paper |
| --- | --- | --- | --- |
| Static Image vs. Static FEA | [Notebook](static_image_vs_fea_significance_tests.ipynb) | [Report](../result-reports/01_static_image_vs_fea.md) | Additional |
| Static FEA vs. Static Multimodal | [Notebook](static_fea_vs_multimodal_significance_tests.ipynb) | [Report](../result-reports/02_static_fea_vs_multimodal.md) | Table 7 |
| Static Image vs. Static Multimodal | [Notebook](static_image_vs_multimodal_significance_tests.ipynb) | [Report](../result-reports/03_static_image_vs_multimodal.md) | Table 7 |

Run the relevant comparison notebook to regenerate its numerical exports in [statistical_results/](statistical_results/). The exported tables include the primary result, paired reenactment data, sensitivity test, participant summaries, and secondary tests where applicable.

The [combined summary](../result-reports/00_summary.md) collects all nine repository comparisons.
