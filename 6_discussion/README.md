# 6. Discussion Analyses

[Repository README](../README.md)

Analyses supporting Section 6 of the paper and the associated supplemental figures. Environment setup, dataset placement, and notebook execution are documented in [env/README.md](../env/README.md).

## Analyses and paper outputs

| Paper section or output | Analysis | Entry point |
| --- | --- | --- |
| 6.1; supplemental Figures S4–S5 | FEA increase positions and coefficient trajectories | [6_1_temporal](6_1_temporal/README.md) |
| 6.2; Figure 5 | Fusion correctness groups, class-wise results, and static–dynamic overlap | [6_2_complementarity](6_2_complementarity/README.md) |
| 6.3; supplemental Figures S6–S7 | Category/error-associated FEA profiles and human annotation agreement | [6_3_interpreting](6_3_interpreting/README.md) |
| Table 7 | Paired model comparisons | [significance-tests](significance-tests/README.md) |

Section 6.4 discusses limitations and implications; it has no separate analysis notebook.

## Shared inputs

- [Static test predictions](../4_static_facial_expression_recognition/static_test_predictions.csv), produced by the [Section 4 collector](../4_static_facial_expression_recognition/collect_static_test_predictions.ipynb).
- [Dynamic test predictions](../5_dynamic_facial_expression_recognition/dynamic_test_predictions.csv), produced by the [Section 5 collector](../5_dynamic_facial_expression_recognition/collect_dynamic_test_predictions.ipynb).
- Raw DFEA split CSVs for the temporal and coefficient-profile analyses, using the dataset layout documented in the environment README.
- The included annotation CSV and FEA/FACS mapping for Section 6.3, documented in its README.

The CSV-based prediction analyses require no trained model files or inference. Each prediction export contains 756 camera-view rows from 378 test reenactments; FEA-only metrics use one prediction per reenactment.

Sequence-order controls remain in [Section 5.1.3](../5_dynamic_facial_expression_recognition/5_1_image/5_1_3_sequence/README.md) and [Section 5.2.3](../5_dynamic_facial_expression_recognition/5_2_fea/5_2_3_sequence/README.md). The shared [confusion-matrix notebook](../supplemental_material/confusion_matrices.ipynb) remains in the supplemental-material folder.
