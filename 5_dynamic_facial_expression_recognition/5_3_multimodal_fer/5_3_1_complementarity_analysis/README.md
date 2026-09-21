# 5.3.1 Complementarity Analysis

[Up one level](../README.md) · [Repository home](../../../README.md)

This analysis compares Image and FEA decisions on paired test samples before inspecting the behavior of the fused model.

## Files

- [Analysis notebook](multimodal_potential_analysis.ipynb).
- [Prediction-case counts](prediction_cases_data.csv).
- [Class and view comparison](prediction_comparison_central_and_side.png).

## Continue with fusion outcomes

The [Discussion multimodal analysis](../../../6_discussion/multimodal-analysis/README.md) evaluates fusion within both-correct, Image-only, FEA-only, and both-wrong groups. A prediction-selection oracle only selects among the unimodal predictions; it is not a strict upper bound for a learned fusion model. Repeated FEA decisions across views are not independent observations.
