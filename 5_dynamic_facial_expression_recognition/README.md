# 5. Dynamic Facial Expression Recognition

[Up one level](../README.md) · [Repository home](../README.md)

This section contains the dynamic baselines and temporal-order experiments introduced by the journal revision.

## Models and experiments

| Area | Entry point | What to find |
|---|---|---|
| 5.1 Image sequences | [Image FER](5_1_image_sequence_based_fer/README.md) | Ordered EfficientNetV2–LSTM, sequence-order controls, significance tests, and prefix trajectories. |
| 5.2 FEA sequences | [FEA FER](5_2_fea_sequence_based_fer/README.md) | Ordered FEA LSTM, sequence-order controls, significance tests, and prefix trajectories. |
| 5.3 Multimodal FER | [Multimodal FER](5_3_multimodal_fer/README.md) | Complementarity, two late-fusion variants, and intermediate fusion. |
| Environment | [Dynamic environment](env/README.md) | Existing Docker and dependency definitions. |

## Comparisons and interpretation

[Section 6](../6_discussion/README.md) contains cross-model significance tests, detailed fusion/error analysis, and FEA signal/annotation analyses. Within-modality order-ablation tests remain alongside their experiments in Sections 5.1 and 5.2.

The current dynamic accuracies are 72.75% for Image, 78.31% for FEA, and 81.61% for intermediate-fusion Multimodal. Each model entry links to its classification report.
