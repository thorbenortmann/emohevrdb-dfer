# Image Prediction Trajectory Analysis

This report summarizes the main descriptive results from the ordered image-LSTM prefix analysis.

## Main findings

The ordered image LSTM becomes more accurate as it receives longer prefixes: 212/756 (28.04%) after one frame and 550/756 (72.75%) after 30 frames. The increase is 44.71 percentage points. This is an exploratory within-model prefix analysis, not a comparison with a separately trained static image model.

| Prefix | Correct / 756 | Accuracy | Mean true-class probability |
| --- | --- | --- | --- |
| 1 | 212/756 | 28.04% | 0.229 |
| 5 | 262/756 | 34.66% | 0.318 |
| 10 | 318/756 | 42.06% | 0.399 |
| 15 | 374/756 | 49.47% | 0.477 |
| 20 | 446/756 | 58.99% | 0.563 |
| 25 | 504/756 | 66.67% | 0.639 |
| 30 | 550/756 | 72.75% | 0.685 |

Figure: `figures/14_class_recall_and_overall_accuracy.png`

*Class-specific recall trajectories with overall accuracy emphasized.*

## Class-specific trajectories

The classes benefit differently from additional frames. Happiness reaches the highest final recall, while Anger remains the most difficult class. Surprise starts especially low and improves strongly over the sequence. The probability trajectories reveal the same heterogeneous evidence accumulation.

| Class | Recall, 1 frame | Recall, 30 frames | Final errors |
| --- | --- | --- | --- |
| Anger | 28.70% | 46.30% | 58 |
| Disgust | 18.52% | 68.52% | 34 |
| Fear | 19.44% | 65.74% | 37 |
| Happiness | 41.67% | 91.67% | 9 |
| Neutral | 44.44% | 75.00% | 27 |
| Sadness | 33.33% | 81.48% | 20 |
| Surprise | 10.19% | 80.56% | 21 |

Figure: `figures/11_mean_true_class_probability.png`

*Mean probability of the ground-truth class for each expression and across all expressions.*

## Final successes and final errors diverge

For the 550 final successes, mean true-class probability rises from 0.257 to 0.903. For the 206 final errors, it changes from 0.154 to 0.102, while mean maximum probability among final errors increases from 0.579 to 0.794. Final errors therefore often become confident incorrect decisions rather than remaining uniformly uncertain.

Figure: `figures/09_trajectories_by_final_outcome.png`

*Mean true-class probability for all view sequences, final successes, and final errors.*

## Competing class hypotheses

The seven-output probability trajectories reveal which alternatives remain competitive as more frames are observed. At the final prefix, Anger remains closely opposed by Disgust, while Surprise remains most strongly opposed by Fear. The most frequent final errors are Anger → Disgust: 45; Surprise → Fear: 19; Fear → Disgust: 18; Disgust → Happiness: 18.

| True class | Mean true-class p, prefix 30 | Strongest competing class | Mean competing p, prefix 30 |
| --- | --- | --- | --- |
| Anger | 0.422 | Disgust | 0.412 |
| Disgust | 0.601 | Happiness | 0.187 |
| Fear | 0.622 | Disgust | 0.168 |
| Happiness | 0.910 | Anger | 0.050 |
| Neutral | 0.706 | Anger | 0.105 |
| Sadness | 0.750 | Anger | 0.152 |
| Surprise | 0.781 | Fear | 0.195 |

Figure: `figures/12_all_class_probabilities_overview.png`

*Mean output probabilities within each ground-truth class across the 30 frame prefixes.*

## Camera-view trajectories

Central and Side views show similar full-sequence accuracy: 73.02% Central and 72.49% Side. The Side view is more accurate over much of the early and middle prefix, while the Central view catches up by the final prefix. Because the two sequences originate from the same reenactments, this comparison is descriptive and paired.

| perspective | prefix_length | accuracy | mean_true_probability |
| --- | --- | --- | --- |
| Central | 1 | 25.93% | 0.218 |
| Central | 10 | 37.83% | 0.372 |
| Central | 20 | 55.03% | 0.533 |
| Central | 30 | 73.02% | 0.690 |
| Side | 1 | 30.16% | 0.240 |
| Side | 10 | 46.30% | 0.427 |
| Side | 20 | 62.96% | 0.592 |
| Side | 30 | 72.49% | 0.679 |

Figure: `figures/15_perspective_trajectories.png`

*Accuracy and mean true-class probability for Central and Side image sequences.*

## Paired Central/Side outcomes

At prefix 30, both views are correct for 62.96% of reenactments; Central alone is correct for 10.05%, Side alone for 9.52%, and both are wrong for 17.46%. The two views predict the same class for 76.19% of reenactments at prefix 30. This shows that the two viewpoints remain partly complementary even though their aggregate accuracies are nearly identical.

Figure: `figures/16_paired_view_correctness.png`

*Paired correctness outcomes and predicted-class agreement between Central and Side views.*

## Probability dynamics within final errors

Across the 206 final errors, the mean probability assigned to the eventual wrong class increases from 0.278 at one frame to 0.794 at 30 frames. Over the same interval, mean probability assigned to the true class changes from 0.154 to 0.102.

Figure: `figures/13_final_error_probabilities_overview.png`

*Mean output probabilities within each ground-truth class, restricted to final errors.*

## Interpretation guardrails

- Prefixes 1–29 are probes of a model trained on 30-frame sequences, not separately optimized early-classification models.
- Prefix positions are not verified onset, apex, or offset phases.
- Central and Side sequences from the same reenactment are paired and should not be treated as independent observations in inferential testing.
- The probability trajectories describe model outputs; they do not establish which visual facial features causally drive the LSTM.
