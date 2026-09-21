# FEA sequence-order ablation

[Up one level](../README.md) · [Repository home](../../../README.md)

This experiment compares the Ordered LSTM with Shuffled LSTM and Mean aggregation controls. The original chronological baseline is linked from the parent modality README.

## Navigate the experiment

- [Paired significance tests](statistical-significance-tests/README.md): final predictions, test notebook, result summary, and statistical tables.
- [Prediction trajectories](trajectories/README.md): frozen ordered-model prefix probes, kept separate from the order-control comparisons.

## Saved training runs

The directory labels below are preserved as stored. The common prediction CSV in the significance-test directory defines the evaluated models' sample-level results.

| Run | Directory |
|---|---|
| Shuffled LSTM; unoptimized run | [20260912-1355](20260912-1355-checkpoint-lstm-shuffled-unoptimzed-b-32-lr-5e-04-seed-31_val_7272_test_6719/README.md) |
| Shuffled LSTM; optimized run | [20260912-1528](20260912-1528-checkpoint-lstm-shuffled-optimzed-c-23-b-32-lr-5e-04-seed-31_val_7636_test_7010/README.md) |
| Mean aggregation; unoptimized run | [20260912-1907](20260912-1907-checkpoint-lstm-mean-unoptimzed-b-32-lr-5e-04-seed-31_val_7740_test_6904/README.md) |

## Interpretation

Chronological models outperform both controls in the supplied paired analyses. These comparisons evaluate separately configured/trained models; they do not isolate temporal order as the sole experimental difference. Prefix probes are not independently retrained sequence-length experiments.
