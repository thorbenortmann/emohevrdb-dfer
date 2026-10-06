# 5.2 FEA Sequences

[Up one level](../README.md) · [Repository README](../../README.md)

[lstm.ipynb](lstm.ipynb) trains and evaluates the ordered FEA LSTM baseline. Its class-wise results support Table 5 (test accuracy: 78.31%).

For setup, see the [environment README](../../env/README.md). A run creates a timestamped directory with `fea_model.keras`, training logs, plots, and evaluation results, then copies the notebook into it.

The saved [classification report](classification_report.txt), [confusion matrix](confusion_matrix.png), and [training history](training_history.png) record the reported run. The selected pretrained checkpoint and its inference filename are documented in [Section 5 models](../models/README.md).

[Section 5.2.3](5_2_3_sequence/README.md) contains Shuffled and Mean controls and the paired sequence-order comparisons.
