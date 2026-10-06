# 5.1 Image Sequences

[Up one level](../README.md) · [Repository README](../../README.md)

[efficientnetv2_lstm.ipynb](efficientnetv2_lstm.ipynb) trains and evaluates the ordered EfficientNetV2–LSTM baseline. Its class-wise results support Table 4 (test accuracy: 72.75%).

For setup, see the [environment README](../../env/README.md). The notebook writes phase checkpoints, training logs, plots, and evaluation results into a new timestamped directory, then copies itself into that directory. The saved [classification report](classification_report.txt), [confusion matrix](confusion_matrix.png), and [training history](training_history.csv) record the reported run.

The selected pretrained checkpoint and its inference filename are documented in [Section 5 models](../models/README.md).

[Section 5.1.3](5_1_3_sequence/README.md) contains the unoptimized and optimized Shuffled and Mean controls, plus the paired sequence-order comparisons.
