# Image prediction trajectories

[Up one level](../README.md) · [Repository home](../../../../README.md)

This analysis probes the frozen Ordered Image model on prefixes of lengths 1–30. It describes the development of class probabilities and predictions within each observed sequence.

## Read the results

- [Integrated trajectory report](outputs/image_trajectory_results_report.md): main entry point for results and interpretation.
- [Companion trajectory summary](image_prediction_trajectory_summary.md).
- [Generated tables and figures](outputs).

## Data and notebooks

1. [Create prediction trajectories](create_image_prediction_trajectories.ipynb) loads the ordered model and original data.
2. [Saved trajectory CSV](image_prediction_trajectories.csv) contains 22,680 rows: 756 view sequences × 30 prefixes.
3. [Analyze saved trajectories](analyze_image_prediction_trajectories.ipynb) generates the descriptive reports and visualizations.

Run from this directory with the configured external paths available for collection. In the trajectory export, `sequence_id` identifies a sequence and `sample_id` identifies a sequence-step row. Final predictions reproduce 550/756 correct decisions.

## Interpretation

Prefixes are probes of a model trained on full sequences. They are not separately validated short-sequence classifiers, causal feature attributions, or annotated expression phases.
