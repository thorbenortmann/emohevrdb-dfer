# 5.1 Image-Sequence-Based FER

[Up one level](../README.md) · [Repository home](../../README.md)

The ordered dynamic baseline uses 30 chronological observations per sequence. Its saved test accuracy is **72.75%**, as documented in the [classification report](classification_report.txt).

## Baseline

- [efficientnetv2_lstm.ipynb](efficientnetv2_lstm.ipynb): training and evaluation.
- [Model download](https://drive.google.com/file/d/1ymkR9QVbyUi1XF4lfTCQIEhoKR-oGkIk/view?usp=sharing): existing repository model link.

## Further experiments

- [Sequence-order ablation](5_1_4_sequence_order_ablation/README.md): Shuffled and Mean controls, paired significance tests, and prefix-trajectory analysis.
- [Discussion analyses](../../6_discussion/README.md): model comparisons, errors, and interpretation.

## Saved baseline results

- [classification_report.txt](classification_report.txt)
- [confusion_matrix.png](confusion_matrix.png)
- [training_history.csv](training_history.csv)
- [training_history.png](training_history.png)
