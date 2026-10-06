# Image sequence-order ablation

[Up one level](../README.md) · [Repository home](../../../README.md)

This experiment compares the Ordered LSTM with Shuffled LSTM and Mean aggregation controls. The original chronological baseline is linked from the parent modality README.

## Navigate the experiment

- [Paired significance tests](significance-tests/README.md): final predictions, test notebook, result summary, and statistical tables.
- [Prediction trajectories](trajectories/README.md): frozen ordered-model prefix probes, kept separate from the order-control comparisons.

## Saved training runs

The directory labels below are preserved as stored. The common prediction CSV in the significance-test directory defines the evaluated models' sample-level results.

| Run | Directory |
|---|---|
| Shuffled LSTM; unoptimized run | [20260913-1135](20260913-1135-checkpoint-efficientnetV2-lstm-shuffled-unoptimized-b-32-lr-1e-03-seed-13_train_8467_val_7051_test_5965/README.md) |
| Shuffled LSTM; optimized run | [20260914-1243](20260914-1243-checkpoint-efficientnetV2-lstm-shuffled-optimized-c-19-b-32-lr-1e-03-seed-13_train_9057_val_7207_test_6190/README.md) |
| Mean aggregation; unoptimized run | [20260914-1416](20260914-1416-checkpoint-efficientnetV2-gap-unoptimized-b-32-lr-1e-03-seed-13_train_8764_val_6766_test_5806/README.md) |
| Mean aggregation; optimized run | [20260914-2006](20260914-2006-checkpoint-efficientnetV2-gap-optimized-c-4-b-32-lr-1e-03-seed-13_train_8675_val_7259_test_6084/README.md) |

## Interpretation

Chronological models outperform both controls in the supplied paired analyses. These comparisons evaluate separately configured/trained models; they do not isolate temporal order as the sole experimental difference. Prefix probes are not independently retrained sequence-length experiments.
