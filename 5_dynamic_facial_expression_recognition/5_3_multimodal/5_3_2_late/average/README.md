# 5.3.2 Late Fusion: Averaging

[Late fusion](../README.md)

[late_fusion_avg.ipynb](late_fusion_avg.ipynb) averages the frozen unimodal probability vectors without training a fusion head. The [classification report](classification_report.txt) records **78.44%** test accuracy; [confusion_matrix.png](confusion_matrix.png) shows class-wise errors.

Use the shared [model setup](../../README.md#model-setup). A run creates a timestamped directory containing `average_model.keras` and evaluation outputs. [Trained-model download](https://drive.google.com/file/d/1yp4o7Ztz3m683ffQVuDqfrUM_p5ydNdT/view?usp=sharing).
