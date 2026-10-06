# 5.3.2 Late Fusion: Cross-Attention

[Up one level](../README.md) · [Repository README](../../../../README.md)

[late_fusion_cross_attention.ipynb](late_fusion_cross_attention.ipynb) trains a cross-attention fusion head over the frozen ordered backbones. The saved test accuracy is **80.56%**.

Use the shared [model setup](../../README.md#model-setup).

## Outputs

Training creates a timestamped results directory with `best_model_by_acc.keras`, logs, plots, and evaluation outputs. The saved [classification report](classification_report.txt) and [confusion matrix](confusion_matrix.png) record the reported experiment. An existing [cross-attention-model download](https://drive.google.com/file/d/1VhxxPBqeUpodqPPWmji41vW4g3KQmmZb/view?usp=sharing) is retained for this experiment.
