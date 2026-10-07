# 5.3.2 Late Fusion: Cross-Attention

[Late fusion](../README.md)

[late_fusion_cross_attention.ipynb](late_fusion_cross_attention.ipynb) trains a cross-attention head over the frozen unimodal probability vectors. The [classification report](classification_report.txt) records **80.56%** test accuracy; [confusion_matrix.png](confusion_matrix.png) shows class-wise errors.

Use the shared [model setup](../../README.md#model-setup). A run creates a timestamped directory containing `best_model_by_acc.keras` and evaluation outputs. [Trained-model download](https://drive.google.com/file/d/1VhxxPBqeUpodqPPWmji41vW4g3KQmmZb/view?usp=sharing).
