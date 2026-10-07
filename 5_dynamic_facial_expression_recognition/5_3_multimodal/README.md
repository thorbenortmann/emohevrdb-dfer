# 5.3 Multimodal Sequence-Based FER

[Section 5](../README.md)

| Paper section | Producer and output |
| --- | --- |
| 5.3.1; Figure 3 | [Prediction complementarity](5_3_1_complementarity/README.md) |
| 5.3.2 | [Late fusion](5_3_2_late/README.md): averaging (78.44%) and cross-attention (80.56%) |
| 5.3.3; Figure 4; Table 6 | [Intermediate fusion](5_3_3_intermediate/README.md): selected Multimodal baseline (81.61%) |

The selected intermediate-fusion predictions are included in [dynamic_test_predictions.csv](../dynamic_test_predictions.csv). Late-fusion results are separate experiments.

## Model setup

Download the ordered Image and FEA checkpoints from [Section 5 models](../models/README.md), then save them as `image_model.keras` and `fea_model.keras` in the relevant experiment's local directory:

| Experiment | Model directory, relative to this folder |
| --- | --- |
| Averaging | `5_3_2_late/average/models/` |
| Late cross-attention | `5_3_2_late/cross_attention/models/` |
| Intermediate fusion | `5_3_3_intermediate/models/` |

Dataset placement and execution are described in [the environment README](../../env/README.md).
