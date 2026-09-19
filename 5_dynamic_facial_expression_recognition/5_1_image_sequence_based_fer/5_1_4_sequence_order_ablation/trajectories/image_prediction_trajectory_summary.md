# Image Prediction Trajectory Analysis — Key Results

## Scope

This README summarizes the trajectory analysis of the **ordered image LSTM** on the EmoHeVRDB test set.

- **756 view sequences** from **378 reenactments**
- Two synchronized views per reenactment: **Central** and **Side**
- **30 ordered frames per view sequence**
- **7 emotion classes**, 54 reenactments per class and 108 view sequences per class
- At prefix length `t`, the LSTM prediction is based on frames `1..t` of one view sequence.
- The trajectory table contains **756 × 30 = 22,680 rows**.
- The model was trained on complete 30-frame sequences; prefixes `1..29` are descriptive probes, not separately trained early-classification models.

## Headline Result

The image LSTM accumulates useful class evidence over the 30-frame window.

| Prefix | Accuracy | Mean true-class probability |
|---:|---:|---:|
| 1 | 28.04% | 0.229 |
| 5 | 34.66% | 0.318 |
| 10 | 42.06% | 0.399 |
| 15 | 49.47% | 0.477 |
| 20 | 58.99% | 0.563 |
| 25 | 66.67% | 0.639 |
| 29 | 71.96% | 0.679 |
| 30 | 72.75% | 0.685 |

The final full-sequence result is **550/756 = 72.75%**.

## Class-Wise Development

| True class | Recall @ 1 | Recall @ 30 |
|---|---:|---:|
| Anger | 28.70% | 46.30% |
| Disgust | 18.52% | 68.52% |
| Fear | 19.44% | 65.74% |
| Happiness | 41.67% | 91.67% |
| Neutral | 44.44% | 75.00% |
| Sadness | 33.33% | 81.48% |
| Surprise | 10.19% | 80.56% |

Important patterns:

- **Happiness** reaches the highest final recall.
- **Anger** remains the most difficult class at the final prefix.
- **Surprise** starts especially low and improves strongly across the sequence.
- The seven classes differ substantially in how quickly useful evidence accumulates.

## Competing Class Hypotheses at Prefix 30

| True class | Mean true-class probability | Strongest competitor | Mean competitor probability |
|---|---:|---|---:|
| Anger | 0.422 | Disgust | 0.412 |
| Disgust | 0.601 | Happiness | 0.187 |
| Fear | 0.622 | Disgust | 0.168 |
| Happiness | 0.910 | Anger | 0.050 |
| Neutral | 0.706 | Anger | 0.105 |
| Sadness | 0.750 | Anger | 0.152 |
| Surprise | 0.781 | Fear | 0.195 |

The most persistent final competition is **Anger vs. Disgust**. Surprise is most strongly opposed by Fear.

## Final Correct vs. Final Incorrect View Sequences

- **550** view sequences are correct at prefix 30.
- **206** are incorrect at prefix 30.

| Group | Mean true-class p @ 1 | Mean true-class p @ 30 | Mean top-1 p @ 1 | Mean top-1 p @ 30 |
|---|---:|---:|---:|---:|
| Final correct | 0.257 | 0.903 | 0.566 | 0.903 |
| Final incorrect | 0.154 | 0.102 | 0.579 | 0.794 |

For the final errors, the mean probability of the **eventual wrong final class** rises from **0.278** at prefix 1 to **0.794** at prefix 30. Final errors therefore often become increasingly confident incorrect decisions rather than remaining simply uncertain.

## Central vs. Side View

| View | Accuracy @ 1 | Accuracy @ 30 | Mean true-class p @ 1 | Mean true-class p @ 30 |
|---|---:|---:|---:|---:|
| Central | 25.93% | 73.02% | 0.218 | 0.690 |
| Side | 30.16% | 72.49% | 0.240 | 0.679 |

At prefix 30, the two views are nearly identical in aggregate accuracy but not redundant at the reenactment level:

- Both views correct: **62.96%** of reenactments
- Central only correct: **10.05%**
- Side only correct: **9.52%**
- Both wrong: **17.46%**
- Same predicted class across views: **76.19%**

The Side view is more accurate over much of the early and middle prefix, whereas the Central view catches up by the full 30-frame sequence.

## Prediction Stability

- Median predicted-class switches per view sequence: **1.0**
- Median final-class stabilization timestep overall: **13.0**
- Median stabilization timestep for final correct sequences: **11.0**
- Median stabilization timestep for final incorrect sequences: **17.5**

Final errors tend to stabilize later and undergo more prediction changes than final successes.

## Main Interpretation

The image LSTM gains substantial predictive evidence as progressively more ordered frames are observed. The temporal development is class-dependent, and final errors frequently consolidate into confident incorrect hypotheses. Central and Side views have almost identical final aggregate accuracy but remain partly complementary for individual reenactments.

These trajectory results complement the separate sequence-order ablation: the ablation tests whether chronology matters, whereas the trajectory analysis describes how the trained ordered model's predictions evolve as additional frames become available.

## Interpretation Guardrails

- Prefix positions must **not** be labeled as verified onset, apex, or offset phases.
- Prefixes 1–29 are not independently optimized early-classification models.
- Central and Side predictions from the same reenactment are paired and should not be treated as statistically independent.
- Prediction trajectories do not by themselves identify which visual facial features causally drive the LSTM.

## Related Artifacts

- `image_prediction_trajectories.csv` — per-view-sequence, per-prefix model predictions
- `create_image_prediction_trajectories.ipynb` — trajectory generation
- `analyze_image_prediction_trajectories.ipynb` — integrated trajectory analysis
- `outputs/image_trajectory_results_report.html` — compact visual report generated by the analysis notebook