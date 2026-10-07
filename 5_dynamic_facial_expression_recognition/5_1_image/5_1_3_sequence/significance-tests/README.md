# Image Sequence-Order Comparisons

[Image controls](../README.md)

[results_summary.md](results_summary.md) records the Section 5.1.3 results: Ordered–Shuffled **+10.85 pp**, CI **[7.28, 14.42]**, and Ordered–Mean **+11.90 pp**, CI **[7.94, 15.87]**. Both Holm-adjusted p-values are below .0001.

[image_sequence_order_significance_tests.ipynb](image_sequence_order_significance_tests.ipynb) reads the included [image_test_predictions.csv](image_test_predictions.csv) and exports [statistical_results/](statistical_results/). It uses a centered paired bootstrap over 378 reenactments, keeping both camera views together. Holm adjustment covers the two primary comparisons; confidence intervals are unadjusted. Participant and view summaries are additional descriptive/sensitivity outputs.

## Regenerate predictions

[collect_image_sequence_order_test_predictions.ipynb](collect_image_sequence_order_test_predictions.ipynb) expects these files in a local `models/` directory:

| Filename | Checkpoint |
| --- | --- |
| `image_sequence_model.keras` | Selected Ordered baseline |
| `image_sequence_shuffled_model.keras` | Selected optimized Shuffled control |
| `image_sequence_mean_model.keras` | Selected optimized Mean control |

The Ordered download is in [Section 5 models](../../../models/README.md); control checkpoints come from the linked training runs. Dataset and execution setup are in [the environment README](../../../../env/README.md).
