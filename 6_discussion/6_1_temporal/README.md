# 6.1 Temporal Modeling under HMD Occlusion

[Discussion](../README.md)

[fea_temporal_analysis.ipynb](fea_temporal_analysis.ipynb) reads all three raw DFEA split CSVs and supports the temporal-heterogeneity discussion and **Figures S4–S5**. No model predictions are needed.

For each non-Neutral category, it selects the coefficient with the highest category mean after averaging the 30 observations within each sequence. Each sequence with a positive increase contributes the position of its largest consecutive increase, taking the earliest tie. The notebook reports eligible counts and the most populated ten-position interval, including the **38.7–47.9%** range discussed in Section 6.1.

## Saved figures

| Supplemental figure | Files in `figures/fea_temporal_analysis/` |
| --- | --- |
| S4: largest-increase positions | [largest_increase_heatmap.pdf](figures/fea_temporal_analysis/largest_increase_heatmap.pdf) |
| S5: six trajectory panels | [Anger](figures/fea_temporal_analysis/trajectories_anger.pdf), [Disgust](figures/fea_temporal_analysis/trajectories_disgust.pdf), [Fear](figures/fea_temporal_analysis/trajectories_fear.pdf), [Happiness](figures/fea_temporal_analysis/trajectories_happiness.pdf), [Sadness](figures/fea_temporal_analysis/trajectories_sadness.pdf), [Surprise](figures/fea_temporal_analysis/trajectories_surprise.pdf) |

Trajectories include all retained sequences, including those without a positive increase. These signals are not aligned to annotated expression phases. Dataset and execution setup are in [the environment README](../../env/README.md).
