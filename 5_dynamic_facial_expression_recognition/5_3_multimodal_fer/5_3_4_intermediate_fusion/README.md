# 5.3.4 Intermediate Fusion

[Up one level](../README.md) · [Repository home](../../../README.md)

The canonical dynamic Multimodal accuracy is **81.61% (617/756)**. The local [classification report](classification_report.txt) is the authoritative result for this model, superseding the previously documented 81.48%.

## Model and notebook

- [intermediate_fusion_cross_attention.ipynb](intermediate_fusion_cross_attention.ipynb): training/evaluation implementation and saved outputs.
- [Model download](https://drive.google.com/file/d/1G5BK0YGuJCS-NiMgNhn8EeHhi19SZSW9/view?usp=sharing): existing repository model link.

## Saved results

- [classification_report.txt](classification_report.txt)
- [confusion_matrix.png](confusion_matrix.png)
- [training_history_accuracy.png](training_history_accuracy.png)
- [training_history_loss.png](training_history_loss.png)
- [training_log.csv](training_log.csv)

## Related analyses

- [Fusion and error analysis](../../../6_discussion/multimodal-analysis/README.md).
- [Dynamic comparison tests](../../../6_discussion/significance-tests/dynamic-significance-tests/README.md).

The Section 6 comparisons use the selected intermediate-fusion model for the dynamic Multimodal setting; the two late-fusion variants are separate experiments.
