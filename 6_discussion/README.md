# 6. Discussion Analyses

[Repository README](../README.md) · [Environment setup](../env/README.md)

| Paper content | Analysis and saved results |
| --- | --- |
| 6.1; Figures S4–S5: temporal variation | [FEA trajectories](6_1_temporal/README.md) |
| 6.2; Figure 5: fusion outcomes, class-wise changes, and dominant confusions | [Prediction complementarity](6_2_complementarity/README.md) |
| 6.3; Figures S6–S7: FEA profiles and annotation agreement | [Persistent error patterns](6_3_interpreting/README.md) |
| Table 7: paired accuracy differences, confidence intervals, and p-values | [Model comparisons](significance-tests/README.md) |

Prediction analyses read the shared [static](../4_static_facial_expression_recognition/static_test_predictions.csv) and/or [dynamic](../5_dynamic_facial_expression_recognition/dynamic_test_predictions.csv) CSVs without model inference. Temporal/profile analyses additionally require raw DFEA split CSVs. Section 6.3 includes its annotation CSV and FEA/FACS mapping.

The separate sequence-order comparisons are in [Section 5.1.3](../5_dynamic_facial_expression_recognition/5_1_image/5_1_3_sequence/README.md) and [Section 5.2.3](../5_dynamic_facial_expression_recognition/5_2_fea/5_2_3_sequence/README.md). Section 6.4 discusses limitations and future work without a separate notebook.
