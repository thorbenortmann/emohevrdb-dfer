# Image Sequence-Order Comparisons

[Up one level](../README.md) · [Repository README](../../../../README.md)

Paired comparisons of Ordered versus optimized Shuffled and Ordered versus optimized Mean, with Holm correction across the two Image comparisons. Image predictions cover 756 views; the primary bootstrap resamples paired reenactments (378 units).

## Execution

1. Run [image_sequence_order_significance_tests.ipynb](image_sequence_order_significance_tests.ipynb) to analyze the included [image_test_predictions.csv](image_test_predictions.csv). This does not require model files or datasets.
2. To regenerate that CSV first, run [collect_image_sequence_order_test_predictions.ipynb](collect_image_sequence_order_test_predictions.ipynb). It uses the test split described in the [environment README](../../../../env/README.md) and expects these checkpoints in this directory's `models/` subfolder:
   - `image_sequence_model.keras`: selected ordered baseline.
   - `image_sequence_shuffled_model.keras`: selected optimized Shuffled control.
   - `image_sequence_mean_model.keras`: selected optimized Mean control.

The ordered-model download is in [Section 5 models](../../../models/README.md). Use the selected control checkpoints from their corresponding training runs. Copy and rename the chosen checkpoints to the filenames above.

The test notebook writes tables into [statistical_results/](statistical_results/). [results_summary.md](results_summary.md) summarizes the saved comparisons. Participant-level and individual-view results are additional sensitivity/descriptive analyses.
