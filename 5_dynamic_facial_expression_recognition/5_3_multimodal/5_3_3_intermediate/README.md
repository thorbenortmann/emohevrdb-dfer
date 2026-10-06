# 5.3.3 Intermediate Fusion

[Up one level](../README.md) · [Repository README](../../../README.md)

[intermediate_fusion_cross_attention.ipynb](intermediate_fusion_cross_attention.ipynb) trains the selected intermediate-fusion Multimodal baseline. The saved test accuracy is **81.61% (617/756)**; class-wise results support Table 6. The [architecture PDF](dfer-intermediate-fusion-compact.pdf) is Figure 4.

Use the shared [model setup](../README.md#model-setup).

## Outputs and checkpoints

Training creates a timestamped results directory with `best_int_fusion_model.keras`, logs, plots, and evaluation outputs. The saved [classification report](classification_report.txt), [confusion matrix](confusion_matrix.png), and [training log](training_log.csv) record the reported run.

An [experiment-model download](https://drive.google.com/file/d/1G5BK0YGuJCS-NiMgNhn8EeHhi19SZSW9/view?usp=sharing) is available. For the shared prediction collector, see [Section 5 models](../../models/README.md).

The shared [dynamic prediction CSV](../../dynamic_test_predictions.csv) supports the complementarity analysis and [Section 6.2 fusion analysis](../../../6_discussion/6_2_complementarity/dynamic_fusion_correctness_groups.ipynb).
