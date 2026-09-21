# FEA Patterns, Annotation Agreement, and Prediction Trajectories

[Up one level](../README.md) · [Repository home](../../README.md)

This analysis family characterizes the 63 recorded FEA channels and relates category, annotation, and temporal patterns to model behavior.

## Analyses

| Step | Question / scope | Implementation | Results |
|---|---|---|---|
| 03 | Channel distributions and aggregation rationale | [Notebook](03_characterize_fea_channels.ipynb) | [Report](outputs/03_fea_channel_characterization/03_fea_channel_characterization_report.md) |
| 04 | Category profiles, semantic groups, and aggregation sensitivity | [Notebook](04_analyze_category_fea_patterns.ipynb) | [Report](outputs/04_category_fea_patterns/category_fea_patterns_report.md) |
| 05 | Correct/incorrect profiles and directed confusion pairs | [Notebook](05_analyze_fea_sequence_model_error_patterns.ipynb) | [Report](outputs/05_fea_sequence_model_error_patterns/fea_sequence_model_error_patterns_report.md) |
| 06 | Annotation agreement and errors across all three dynamic modalities | [Notebook](06_analyze_label_agreement_and_model_errors.ipynb) | [Report](outputs/06_label_agreement_and_model_errors/label_agreement_and_model_errors_report.md) |
| 07 | Chronological/event-aligned FEA signals and prediction transitions | [Notebook](07_analyze_fea_and_prediction_trajectories.ipynb) | [Report](outputs/07_fea_and_prediction_trajectories/fea_and_prediction_trajectories_report.md) |

Each report points to its detailed tables and visualizations in the corresponding [output directory](outputs). The step numbers identify analyses within this workflow, not manuscript section numbers.

## Inputs and suggested workflow

1. Inspect the [data and mapping guide](data/README.md) and run [the canonical dataset generator](create_canonical_fea_analysis_datasets.ipynb) if the six input CSVs have not been generated locally.
2. Follow 03 → 04 for signal characterization and category profiles; use 05 for test-set error profiles.
3. Notebook 06 has an independent input route with embedded annotation, prediction, and membership snapshots plus optional file overrides. Its output provenance tables identify the inputs used.
4. Notebook 07 combines canonical FEA sequences with the [ordered FEA prediction trajectories](../../5_dynamic_facial_expression_recognition/5_2_fea_sequence_based_fer/5_2_4_sequence_order_ablation/trajectories/README.md). Consult its path settings before running.

Run these notebooks from this directory. Raw FEA characterization can combine the 1,727 Train/Validation/Test reenactments from 36 participants. Model-linked errors and prediction analyses use the held-out 378 reenactments from eight participants. The six canonical input CSVs are generated locally and are not included in this snapshot; their saved validation record is linked from the data guide.

## Interpretation

- FEAs are proprietary coefficients; the FACS mapping is a semantic crosswalk, not validated AU measurement.
- Sample weighting, participant balancing, participant-specific Neutral centering, and channel standardization are distinct operations.
- Chronological sequence positions are not annotated expression phases. Secondary event alignment uses observed signal/probability transitions.
- Coefficient differences and temporal associations are descriptive; they do not establish causal model reliance. No separate group-perturbation/model-reliance experiment is included here.
- Annotation disagreement is not proof of an incorrect label; class composition and participant coverage matter.

For fusion-specific outcomes see [multimodal error analysis](../multimodal-analysis/README.md); for inferential model comparisons see [significance tests](../significance-tests/README.md).
