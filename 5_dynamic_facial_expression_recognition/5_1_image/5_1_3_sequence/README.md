# 5.1.3 Image Sequence-Order Controls

[Up one level](../README.md) · [Repository README](../../../README.md)

Compare the ordered Image baseline against Shuffled frame order and Mean pooling over frame features. The initial and tuned controls are retained to show the effect of optimization.

| Saved control run | Test accuracy |
| --- | --- |
| [Shuffled, unoptimized](20260913-1135-checkpoint-efficientnetV2-lstm-shuffled-unoptimized-b-32-lr-1e-03-seed-13_train_8467_val_7051_test_5965/README.md) | 59.66% |
| [Shuffled, optimized](20260914-1243-checkpoint-efficientnetV2-lstm-shuffled-optimized-c-19-b-32-lr-1e-03-seed-13_train_9057_val_7207_test_6190/README.md) | 61.90% |
| [Mean, unoptimized](20260914-1416-checkpoint-efficientnetV2-gap-unoptimized-b-32-lr-1e-03-seed-13_train_8764_val_6766_test_5806/README.md) | 58.07% |
| [Mean, optimized](20260914-2006-checkpoint-efficientnetV2-gap-optimized-c-4-b-32-lr-1e-03-seed-13_train_8675_val_7259_test_6084/README.md) | 60.85% |

The ordered baseline is in [Section 5.1](../README.md). [results.txt](results.txt) summarizes validation and test results. Each run folder contains its training notebook and saved evaluation outputs.

Use [significance-tests](significance-tests/README.md) for predictions and paired comparisons of Ordered versus the selected optimized Shuffled and Mean controls. These comparisons support the sequence-order analysis in Section 5.1.3.
