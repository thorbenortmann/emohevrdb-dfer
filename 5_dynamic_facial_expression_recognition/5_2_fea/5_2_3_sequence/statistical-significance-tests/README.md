# FEA Sequence-Order Comparisons

[FEA controls](../README.md)

[results_summary.md](results_summary.md) records the Section 5.2.3 results: Ordered–Shuffled **+8.20 pp**, CI **[4.76, 11.90]**, and Ordered–Mean **+9.26 pp**, CI **[5.82, 12.96]**. Both Holm-adjusted p-values are below .0001.

[fea_sequence_order_significance_tests.ipynb](fea_sequence_order_significance_tests.ipynb) reads the included [fea_test_predictions.csv](fea_test_predictions.csv) and exports [statistical_results/](statistical_results/). It uses exact paired McNemar tests on 378 reenactments and paired-bootstrap confidence intervals. Holm adjustment covers the two primary comparisons; confidence intervals are unadjusted. Participant and sensitivity results are additional outputs.

## Regenerate predictions

[collect_fea_sequence_order_test_predictions.ipynb](collect_fea_sequence_order_test_predictions.ipynb) expects these files in `../models/`, relative to this directory:

| Filename | Checkpoint |
| --- | --- |
| `fea_sequence_model.keras` | Selected Ordered baseline |
| `fea_sequence_shuffled_model.keras` | Selected optimized Shuffled control |
| `fea_sequence_mean_model.keras` | Selected Mean control |

The Ordered download is in [Section 5 models](../../../models/README.md); control checkpoints come from the linked training runs. The collector uses seed 33 for test-sequence shuffling. Dataset and execution setup are in [the environment README](../../../../env/README.md).
