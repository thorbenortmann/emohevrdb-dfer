# 5.3.3 Intermediate Fusion

[Multimodal FER](../README.md)

[intermediate_fusion_cross_attention.ipynb](intermediate_fusion_cross_attention.ipynb) trains the selected Multimodal baseline using frozen unimodal feature extractors and a trainable cross-attention fusion head.

| Reported content | Source |
| --- | --- |
| Table 6; 81.61% test accuracy (617/756) | [classification_report.txt](classification_report.txt) |
| Figure 4: architecture | [dfer-intermediate-fusion-compact.pdf](dfer-intermediate-fusion-compact.pdf) |
| Tables S9–S11: augmentation, architecture, and training settings | Notebook |
| Training/evaluation records | [training_log.csv](training_log.csv) and [confusion_matrix.png](confusion_matrix.png) |

Use the shared [model setup](../README.md#model-setup). Training writes a timestamped directory with `best_int_fusion_model.keras` and evaluation outputs. The inference checkpoint is linked in [Section 5 models](../../models/README.md).

[Shared dynamic predictions](../../dynamic_test_predictions.csv) provide the input for [Section 6](../../../6_discussion/README.md).
