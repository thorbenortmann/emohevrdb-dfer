# 5.3.1 Prediction Complementarity

[Up one level](../README.md) · [Repository README](../../../README.md)

[dfer_prediction_overlap.ipynb](dfer_prediction_overlap.ipynb) computes the four correctness groups for the ordered Image and FEA models and produces Figure 3. It reads [dynamic_test_predictions.csv](../../dynamic_test_predictions.csv); no raw datasets or model files are needed.

Counts are view-level: each of the 378 reenactments contributes two Image–FEA comparisons, giving 756 comparisons. The single FEA prediction is paired with both views. The notebook also reports the prediction-selection oracle.

Saved outputs are [prediction_cases_data.csv](prediction_cases_data.csv) and the [PDF](figures/dfer_prediction_overlap.pdf) / [PNG](figures/dfer_prediction_overlap.png) figure.

For correctness-group analyses involving the fused model, see [Section 6.2](../../../6_discussion/6_2_complementarity/dynamic_fusion_correctness_groups.ipynb).
