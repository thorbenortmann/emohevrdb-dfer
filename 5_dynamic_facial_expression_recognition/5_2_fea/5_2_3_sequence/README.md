# 5.2.3 FEA Sequence-Order Controls

[Ordered baseline](../README.md)

Mean averages the 30 FEA vectors before classification; Shuffled preserves the recurrent architecture but shuffles observation order. The optimized Shuffled run and the Mean run are the controls used in the paper. The initial Mean configuration remained best after optimization.

| Saved control run | Test accuracy |
| --- | --- |
| [Shuffled, unoptimized](20260912-1355-checkpoint-lstm-shuffled-unoptimzed-b-32-lr-5e-04-seed-31_val_7272_test_6719/README.md) | 67.20% |
| [Shuffled, optimized](20260912-1528-checkpoint-lstm-shuffled-optimzed-c-23-b-32-lr-5e-04-seed-31_val_7636_test_7010/README.md) | 70.11% |
| [Mean](20260912-1907-checkpoint-lstm-mean-unoptimzed-b-32-lr-5e-04-seed-31_val_7740_test_6904/README.md) | 69.05% |

[results.txt](results.txt) records validation/test accuracies and tuning budgets. Each run README links to its training notebook and evaluation report.

[Paired comparisons](statistical-significance-tests/README.md) provide the prediction export, producer notebook, numerical tables, and summary for the reported Ordered–Shuffled and Ordered–Mean differences and confidence intervals.
