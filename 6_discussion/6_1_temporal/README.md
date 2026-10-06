# 6.1 Temporal Modeling under HMD Occlusion

[Up one level](../README.md) · [Repository README](../../README.md)

[fea_temporal_analysis.ipynb](fea_temporal_analysis.ipynb) supports the temporal-heterogeneity discussion and produces supplemental Figures S4–S5. It reads the three raw DFEA split CSVs using the [shared environment setup](../../env/README.md); no prediction CSV or model checkpoint is needed.

All retained training, validation, and test sequences are pooled. For each non-Neutral category, the notebook selects the coefficient with the highest category mean, after averaging the 30 observations within each sequence. The largest strictly positive consecutive increase contributes its destination position, with the earliest position used for ties. Category-mean and individual trajectories include all sequences, including those without a positive increase.

## Saved figures

| Supplemental figure | Files in `figures/fea_temporal_analysis/` |
| --- | --- |
| S4: largest-increase positions | [largest_increase_heatmap.pdf](figures/fea_temporal_analysis/largest_increase_heatmap.pdf) |
| S5: six trajectory panels | [Anger](figures/fea_temporal_analysis/trajectories_anger.pdf), [Disgust](figures/fea_temporal_analysis/trajectories_disgust.pdf), [Fear](figures/fea_temporal_analysis/trajectories_fear.pdf), [Happiness](figures/fea_temporal_analysis/trajectories_happiness.pdf), [Sadness](figures/fea_temporal_analysis/trajectories_sadness.pdf), [Surprise](figures/fea_temporal_analysis/trajectories_surprise.pdf) |

The notebook displays the selected coefficients, eligible-sequence counts, and the most populated ten-position intervals. These transitions describe recorded coefficient variation; the sequences have no annotated onset, apex, or offset phases.

Static–dynamic accuracy comparisons are in [significance-tests](../significance-tests/README.md); sequence-order controls are documented in Section 5.
