# 5.3.2 Late Fusion

[Multimodal FER](../README.md)

These experiments combine the frozen models' seven-class prediction vectors.

| Method | Test accuracy | Notebook and results |
| --- | ---: | --- |
| Average probabilities | 78.44% | [Averaging](average/README.md) |
| Learned cross-attention | 80.56% | [Cross-attention](cross_attention/README.md) |

Checkpoint placement is documented once in [model setup](../README.md#model-setup). The selected Multimodal baseline is the separately evaluated [intermediate-fusion model](../5_3_3_intermediate/README.md).
