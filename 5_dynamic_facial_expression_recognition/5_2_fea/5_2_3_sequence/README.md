# 5.2.3 FEA Sequence-Order Controls

[Up one level](../README.md) · [Repository README](../../../README.md)

Compare the ordered FEA baseline against Shuffled sequence order and Mean pooling over the FEA sequence.

| Saved control run | Test accuracy |
| --- | --- |
| [Shuffled, unoptimized](20260912-1355-checkpoint-lstm-shuffled-unoptimzed-b-32-lr-5e-04-seed-31_val_7272_test_6719/README.md) | 67.20% |
| [Shuffled, optimized](20260912-1528-checkpoint-lstm-shuffled-optimzed-c-23-b-32-lr-5e-04-seed-31_val_7636_test_7010/README.md) | 70.11% |
| [Mean](20260912-1907-checkpoint-lstm-mean-unoptimzed-b-32-lr-5e-04-seed-31_val_7740_test_6904/README.md) | 69.05% |

For Mean, the initial configuration remained best after optimization, so the same saved run represents the selected control. The unoptimized Shuffled run is retained to show the tuning improvement.

The ordered baseline is in [Section 5.2](../README.md). [results.txt](results.txt) summarizes validation and test results. Use [statistical-significance-tests](statistical-significance-tests/README.md) for predictions and paired comparisons of Ordered versus the selected Shuffled and Mean controls.
