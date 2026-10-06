# 5.3 Multimodal Fusion

[Up one level](../README.md) · [Repository README](../../README.md)

Combine the selected ordered Image and FEA sequence models.

| Paper section | Analysis or experiment |
| --- | --- |
| 5.3.1 | [Prediction complementarity](5_3_1_complementarity/README.md), computed from the shared dynamic prediction CSV |
| 5.3.2 | [Late fusion](5_3_2_late/README.md): averaging and cross-attention |
| 5.3.3 | [Intermediate fusion](5_3_3_intermediate/README.md): selected Multimodal baseline |

For the runtime and dataset layout, see the [environment README](../../env/README.md).

## Model setup

Download the selected ordered Image and FEA checkpoints using the links in [Section 5 models](../models/README.md). Copy them as `image_model.keras` and `fea_model.keras` into each experiment's local model directory:

| Experiment | Model directory, relative to this folder |
| --- | --- |
| Late fusion: averaging | `5_3_2_late/average/models/` |
| Late fusion: cross-attention | `5_3_2_late/cross_attention/models/` |
| Intermediate fusion | `5_3_3_intermediate/models/` |

The selected intermediate-fusion predictions are included in [dynamic_test_predictions.csv](../dynamic_test_predictions.csv) and used in the Section 6 analyses. Late-fusion models remain separate experiments.
