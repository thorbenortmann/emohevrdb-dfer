# 5.1.3 Image Control: Shuffled, optimized

[Up one level](../README.md) · [Repository README](../../../../README.md)

The selected configuration after tuning the shuffled-order control. The saved run has test accuracy **61.90%**.

The training notebook is [efficientnetV2-lstm-shuffled-optimized.ipynb](efficientnetV2-lstm-shuffled-optimized.ipynb). A rerun creates a new timestamped subdirectory here; it does not resume the saved run automatically.

[classification_report.txt](classification_report.txt) and [confusion_matrix.png](confusion_matrix.png) contain the saved evaluation. Training histories and phase logs are retained alongside the notebook. The training notebook generates `.keras` checkpoints locally.
