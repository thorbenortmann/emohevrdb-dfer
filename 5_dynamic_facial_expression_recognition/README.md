# 5. Dynamic Facial Expression Recognition

[Repository README](../README.md) · [Environment setup](../env/README.md)

## Paper outputs and experiments

| Paper content | Producer and saved results |
| --- | --- |
| Section 5.1; Table 4: ordered Image model | [Image sequences](5_1_image/README.md) |
| Section 5.1.3: Image sequence-order controls and paired tests | [Image controls](5_1_image/5_1_3_sequence/README.md) |
| Section 5.2; Table 5: ordered FEA model | [FEA sequences](5_2_fea/README.md) |
| Section 5.2.3: FEA sequence-order controls and paired tests | [FEA controls](5_2_fea/5_2_3_sequence/README.md) |
| Section 5.3.1; Figure 3: unimodal correctness overlap | [Complementarity](5_3_multimodal/5_3_1_complementarity/README.md) |
| Section 5.3.2: late-fusion accuracies | [Late fusion](5_3_multimodal/5_3_2_late/README.md) |
| Section 5.3.3; Figure 4; Table 6: selected Multimodal model | [Intermediate fusion](5_3_multimodal/5_3_3_intermediate/README.md) |

Supplemental Tables S4–S11 document the baseline configurations; Figure S3 shows their confusion matrices. See the [supplement index](../supplemental_material/README.md).

## Shared test predictions

[collect_dynamic_test_predictions.ipynb](collect_dynamic_test_predictions.ipynb) runs the selected ordered Image, ordered FEA, and intermediate-fusion Multimodal models and exports [dynamic_test_predictions.csv](dynamic_test_predictions.csv). Checkpoint filenames and downloads are in [models/README.md](models/README.md).

The included CSV supplies the complementarity and [Section 6 analyses](../6_discussion/README.md) without inference. Evaluation units and class order are documented in the [repository README](../README.md#shared-predictions). Sequence-order tests use separate prediction exports linked from their control sections.
