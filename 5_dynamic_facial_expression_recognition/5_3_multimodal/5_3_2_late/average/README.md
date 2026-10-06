# 5.3.2 Late Fusion: Averaging

[Up one level](../README.md) · [Repository README](../../../../README.md)

[late_fusion_avg.ipynb](late_fusion_avg.ipynb) averages the two models' class probabilities without training a fusion head. The saved test accuracy is **78.44%**.

Use the shared [model setup](../../README.md#model-setup).

## Outputs

The notebook creates a timestamped results directory and saves `average_model.keras` and evaluation outputs. The saved [classification report](classification_report.txt) and [confusion matrix](confusion_matrix.png) record the reported experiment. An existing [averaging-model download](https://drive.google.com/file/d/1yp4o7Ztz3m683ffQVuDqfrUM_p5ydNdT/view?usp=sharing) is retained for this experiment.
