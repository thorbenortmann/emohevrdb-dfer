# Image sequence-order significance tests

[Up one level](../README.md) · [Repository home](../../../../README.md)

Start with the [results summary](results_summary.md). It reports Ordered versus Shuffled and Ordered versus Mean, with Holm correction across these two primary tests within the Image modality.

## Files and execution order

1. [Collect test predictions](collect_image_sequence_order_test_predictions.ipynb) if a new inference export is needed. This requires the datasets and three trained models configured in the notebook.
2. [image_test_predictions.csv](image_test_predictions.csv) is the saved common input.
3. [Run paired significance tests](image_sequence_order_significance_tests.ipynb) to regenerate statistical outputs from that CSV.
4. [Statistical tables](statistical_results) contains primary results, paired reenactment tables, participant summaries, sensitivity tests, and Holm-adjustment results.

Run the notebooks from this directory after checking their path settings. The CSV is already included; reading or reanalyzing the saved predictions does not require rerunning model inference.

## Evaluation unit

Image uses 756 view predictions from 378 reenactments. The primary centered bootstrap resamples reenactments, retaining their Central and Side views together.

Participant summaries are descriptive; these primary tests do not model additional dependence between reenactments from the same participant.

For chronological prefix behavior, continue to [prediction trajectories](../trajectories/README.md).
