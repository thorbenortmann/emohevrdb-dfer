# FEA Prediction Trajectory Analysis — Key Results

## Scope

This README summarizes the trajectory analysis of the **ordered FEA LSTM** on the EmoHeVRDB test set.

- **378 test sequences**
- **30 ordered FEA observations per sequence**
- **7 emotion classes**, 54 sequences per class
- At prefix length `t`, the model receives observations `1..t` and produces one 7-class prediction.
- The trajectory table therefore contains **378 × 30 = 11,340 prediction rows**.
- The model was trained on full 30-observation sequences. Prefix predictions for `t < 30` are therefore an analysis of the trained model under shorter inputs, not separately optimized early-classification models.

The sequence prefixes should **not** be interpreted as verified onset/apex/offset phases; no such phase annotations are available.

## Headline Result

The ordered FEA LSTM accumulates useful class evidence over the sequence window.

| Prefix length | Accuracy | Mean true-class probability |
|---:|---:|---:|
| 1 | 29.10% | 0.216 |
| 5 | 37.04% | 0.338 |
| 10 | 46.03% | 0.427 |
| 15 | 52.65% | 0.507 |
| 20 | 65.34% | 0.608 |
| 25 | 74.60% | 0.699 |
| 29 | 79.10% | 0.721 |
| 30 | **78.31%** | **0.720** |

The final full-sequence result is **296/378 correct = 78.31%**.

Accuracy is not strictly monotonic: prefix 29 is slightly higher than prefix 30. This should not be interpreted as evidence that 29 observations are globally optimal, because the model was trained for 30-observation sequences.

## Class-Wise Development

Class-wise recall changes substantially over the sequence.

| True class | Recall @ 1 | Recall @ 30 |
|---|---:|---:|
| Anger | 18.52% | 51.85% |
| Disgust | 7.41% | 55.56% |
| Fear | 22.22% | 61.11% |
| Happiness | 40.74% | 100.00% |
| Neutral | 74.07% | 94.44% |
| Sadness | 31.48% | 88.89% |
| Surprise | 9.26% | 96.30% |

Important patterns:

- **Neutral** is already comparatively recognizable from very short prefixes.
- **Surprise** starts very poorly but improves strongly across the sequence.
- **Happiness** reaches perfect final recall.
- **Anger, Disgust, and Fear** remain the most difficult classes at the end of the sequence.

The class-wise mean true-class probability trajectories show the same general pattern and provide a smoother view than recall alone.

## Competing Class Hypotheses

The full 7-class probability trajectories show how competing hypotheses evolve over time.

At prefix 30, the strongest competing class for several difficult categories is:

| True class | Mean true-class probability | Strongest competitor | Mean competitor probability |
|---|---:|---|---:|
| Anger | 0.476 | Disgust | 0.442 |
| Disgust | 0.525 | Happiness | 0.177 |
| Fear | 0.506 | Surprise | 0.251 |
| Happiness | 0.999 | Anger | 0.0003 |
| Neutral | 0.855 | Happiness | 0.052 |
| Sadness | 0.858 | Disgust | 0.070 |
| Surprise | 0.824 | Fear | 0.149 |

The most notable persistent competition is **Anger vs. Disgust**. Fear and Surprise also remain related competitors. These patterns are consistent with the known final confusion structure of the FEA LSTM.

## Final Correct vs. Final Incorrect Sequences

The strongest trajectory contrast appears when sequences are split by their final 30-step outcome.

- **296 sequences** are correct at prefix 30.
- **82 sequences** are incorrect at prefix 30.

### Mean true-class probability

| Group | Prefix 1 | Prefix 30 |
|---|---:|---:|
| Final correct | 0.237 | **0.890** |
| Final incorrect | 0.139 | **0.108** |

For finally correct sequences, evidence for the true class increases strongly. For finally incorrect sequences, true-class probability stays low and even decreases slightly on average.

### True-class margin

The true-class margin is

`P(true class) - max(P(any incorrect class))`.

| Prefix | Final correct | Final incorrect |
|---:|---:|---:|
| 1 | -0.039 | -0.230 |
| 5 | -0.037 | -0.530 |
| 10 | +0.120 | -0.620 |
| 15 | +0.297 | -0.604 |
| 20 | +0.516 | -0.599 |
| 25 | +0.724 | -0.644 |
| 30 | **+0.795** | **-0.699** |

This suggests two qualitatively different trajectories:

- Finally correct sequences increasingly favor the true class.
- Finally incorrect sequences often become increasingly committed to an incorrect hypothesis rather than remaining merely uncertain.

For the 82 final errors, the mean probability of the **eventual incorrect final class** rises from **0.230 at prefix 1** to **0.807 at prefix 30**.

## Prediction Composition Over Time

The model is strongly biased toward **Neutral** for very short prefixes.

Predicted classes at prefix 1:

| Predicted class | Count |
|---|---:|
| Anger | 20 |
| Disgust | 21 |
| Fear | 66 |
| Happiness | 75 |
| Neutral | **162** |
| Sadness | 24 |
| Surprise | 10 |

At prefix 30 the prediction distribution is much more balanced:

| Predicted class | Count |
|---|---:|
| Anger | 30 |
| Disgust | 62 |
| Fear | 43 |
| Happiness | 70 |
| Neutral | 61 |
| Sadness | 50 |
| Surprise | 62 |

This early Neutral bias is descriptive only. It should not be interpreted as evidence that the first observations correspond to a verified neutral/onset phase.

## Prediction Stability

Prediction trajectories are generally not highly volatile.

- Median number of predicted-class switches per sequence: **1**
- Median earliest timestep after which the final predicted class never changes again:
  - **9** for finally correct sequences
  - **17.5** for finally incorrect sequences

Thus, correct sequences tend to settle on their final class earlier than incorrect sequences, although both groups usually change predicted class only a small number of times.

## Main Interpretation

The trajectory analysis supports the conclusion that the ordered FEA LSTM does not make its final decision from a single observation. Instead, class evidence develops across the 30-observation window, and the pattern differs strongly between emotion categories.

The most important findings are:

1. Overall accuracy and mean true-class probability increase substantially with additional ordered observations.
2. Temporal development differs strongly by class, especially for Neutral, Surprise, Happiness, Anger, Disgust, and Fear.
3. Typical class competitions such as Anger–Disgust and Fear–Surprise remain visible in the probability trajectories.
4. Finally correct sequences progressively accumulate evidence for the true class.
5. Finally incorrect sequences frequently become increasingly confident in a wrong class instead of merely remaining uncertain.
6. Correct sequences tend to stabilize on their final prediction earlier than incorrect sequences.

These results complement the separate **sequence-order ablation**, which showed that the chronological ordering itself carries predictive information compared with shuffled or mean-aggregated alternatives.

## Interpretation Guardrails

Do **not** infer from these analyses that:

- specific timesteps correspond to onset, apex, or offset;
- the LSTM has learned a particular facial-action phase sequence;
- prefix 29 is the optimal sequence length because its observed test accuracy is slightly above prefix 30;
- FEA coefficients directly measure physiological muscle activation.

The trajectory results are descriptive analyses of model predictions over progressively longer ordered prefixes.

## Related Artifacts

Primary analysis artifacts:

- `fea_prediction_trajectories.csv` — per-sequence, per-prefix prediction trajectories
- `create_fea_prediction_trajectories.ipynb` — trajectory generation
- `analyze_fea_prediction_trajectories.ipynb` — integrated trajectory analysis
- `fea_trajectory_results_report.html` — compact visual report

The analysis notebook also exports detailed figures and CSV summaries for class-wise recall, true-class probabilities, class-probability competition, final-error trajectories, confusion matrices, prediction stability, participant-level summaries, and representative sequence examples.
