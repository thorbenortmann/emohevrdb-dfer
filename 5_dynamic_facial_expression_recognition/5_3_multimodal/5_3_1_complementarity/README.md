# 5.3.1 Prediction Complementarity

[Multimodal FER](../README.md)

[dfer_prediction_overlap.ipynb](dfer_prediction_overlap.ipynb) reads [dynamic_test_predictions.csv](../../dynamic_test_predictions.csv) and computes the Section 5.3.1 overlap counts and **Figure 3**. No raw datasets or checkpoints are needed.

The 756 view comparisons comprise 476 jointly correct, 116 FEA-only correct, 74 Image-only correct, and 90 jointly incorrect cases. Pairing each reenactment's FEA prediction with both views yields prediction-selection coverage of 666/756 = 88.10%.

Saved outputs: [prediction_cases_data.csv](prediction_cases_data.csv) and [Figure 3 PDF](figures/dfer_prediction_overlap.pdf). The [Section 6.2 notebook](../../../6_discussion/6_2_complementarity/README.md) evaluates fusion outcomes within these groups.
