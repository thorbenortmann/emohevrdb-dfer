# FEA prediction trajectories

[Up one level](../README.md) · [Repository home](../../../../README.md)

This analysis probes the frozen Ordered FEA model on prefixes of lengths 1–30. It describes the development of class probabilities and predictions within each observed sequence.

## Read the results

- [Integrated trajectory report](outputs/fea_trajectory_results_report.md): main entry point for results and interpretation.
- [Companion trajectory summary](fea_prediction_trajectory_summary.md).
- [Generated tables and figures](outputs).

## Data and notebooks

1. [Create prediction trajectories](create_fea_prediction_trajectories.ipynb) loads the ordered model and original data.
2. [Saved trajectory CSV](fea_prediction_trajectories.csv) contains 11,340 rows: 378 reenactments × 30 prefixes.
3. [Analyze saved trajectories](analyze_fea_prediction_trajectories.ipynb) generates the descriptive reports and visualizations.

Run from this directory with the configured external paths available for collection. In the trajectory export, `sequence_id` identifies a sequence and `sample_id` identifies a sequence-step row. Final predictions reproduce 296/378 correct decisions.

## Interpretation

Prefixes are probes of a model trained on full sequences. They are not separately validated short-sequence classifiers, causal feature attributions, or annotated expression phases. For the relationship between raw FEA signals and prediction trajectories, see [FEA analysis, notebook 07](../../../../6_discussion/fea_analysis/README.md).
