# 5.3.2 Late Fusion

[Up one level](../README.md) · [Repository README](../../../README.md)

Two late-fusion experiments combine the ordered Image and FEA sequence models:

| Experiment | Test accuracy | Notebook |
| --- | --- | --- |
| Average of class probabilities | 78.44% | [average](average/README.md) |
| Cross-attention fusion | 80.56% | [cross_attention](cross_attention/README.md) |

Each experiment keeps its notebook, classification report, and confusion matrix in its own folder. Both use the shared [model setup](../README.md#model-setup).

The selected Multimodal baseline is the [intermediate-fusion model](../5_3_3_intermediate/README.md), evaluated separately in Section 5.3.3.
