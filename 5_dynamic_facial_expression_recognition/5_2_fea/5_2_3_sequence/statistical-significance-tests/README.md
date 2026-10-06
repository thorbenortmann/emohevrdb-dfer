# FEA Sequence-Order Comparisons

[Up one level](../README.md) · [Repository README](../../../../README.md)

Paired comparisons of Ordered versus optimized Shuffled and Ordered versus selected Mean on 378 reenactments. The primary test is exact paired McNemar; paired bootstrap intervals describe accuracy differences. Holm correction covers the two FEA comparisons.

## Execution

1. Run [fea_sequence_order_significance_tests.ipynb](fea_sequence_order_significance_tests.ipynb) to analyze the included [fea_test_predictions.csv](fea_test_predictions.csv). This does not require model files or datasets.
2. To regenerate that CSV first, run [collect_fea_sequence_order_test_predictions.ipynb](collect_fea_sequence_order_test_predictions.ipynb). It uses the test split described in the [environment README](../../../../env/README.md) and expects these checkpoints in `../models/` (the `5_2_3_sequence/models/` directory):
   - `fea_sequence_model.keras`: selected ordered baseline.
   - `fea_sequence_shuffled_model.keras`: selected optimized Shuffled control.
   - `fea_sequence_mean_model.keras`: selected Mean control.

The ordered-model download is in [Section 5 models](../../../models/README.md). Use the selected control checkpoints from their corresponding training runs. Copy and rename the chosen checkpoints to the filenames above. The collector uses seed 33 for the test sequence shuffle.

The test notebook writes tables into [statistical_results/](statistical_results/). [results_summary.md](results_summary.md) summarizes the saved comparisons. Participant summaries and sensitivity tests are additional analyses.
