# 5.1.3 Image Sequence-Order Controls

[Ordered baseline](../README.md)

Mean pools the 30 frame-feature vectors; Shuffled preserves the recurrent architecture but shuffles frame order. The optimized Shuffled and Mean runs are the controls used in the paper; initial runs show the optimization improvement.

| Saved control run | Test accuracy |
| --- | --- |
| [Shuffled, unoptimized](20260913-1135-checkpoint-efficientnetV2-lstm-shuffled-unoptimized-b-32-lr-1e-03-seed-13_train_8467_val_7051_test_5965/README.md) | 59.66% |
| [Shuffled, optimized](20260914-1243-checkpoint-efficientnetV2-lstm-shuffled-optimized-c-19-b-32-lr-1e-03-seed-13_train_9057_val_7207_test_6190/README.md) | 61.90% |
| [Mean, unoptimized](20260914-1416-checkpoint-efficientnetV2-gap-unoptimized-b-32-lr-1e-03-seed-13_train_8764_val_6766_test_5806/README.md) | 58.07% |
| [Mean, optimized](20260914-2006-checkpoint-efficientnetV2-gap-optimized-c-4-b-32-lr-1e-03-seed-13_train_8675_val_7259_test_6084/README.md) | 60.85% |

[results.txt](results.txt) records validation/test accuracies and tuning budgets. Each run README links to its training notebook and evaluation report.

[Paired comparisons](significance-tests/README.md) provide the prediction export, producer notebook, numerical tables, and summary for the reported Ordered–Shuffled and Ordered–Mean differences and confidence intervals.
