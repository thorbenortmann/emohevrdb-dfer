# Section 6.2 — Descriptive results

Generated (UTC): 2026-10-06T19:52:44.981395+00:00

## Fusion outcomes

| group | n | correct | wrong | correct_percent |
| --- | --- | --- | --- | --- |
| both_correct | 476 | 474 | 2 | 99.5798 |
| image_only_correct | 74 | 52 | 22 | 70.2703 |
| fea_only_correct | 116 | 86 | 30 | 74.1379 |
| both_wrong | 90 | 5 | 85 | 5.5556 |

- Jointly correct cases preserved: 474/476.
- Exactly-one-correct cases resolved: 138/190 = 72.63%.
- Both-wrong cases recovered: 5/90.

## Dynamic class-wise recall and fusion differences

| emotion | image_recall_percent | fea_recall_percent | multimodal_recall_percent | fusion_minus_image_pp | fusion_minus_fea_pp | fusion_minus_stronger_unimodal_pp |
| --- | --- | --- | --- | --- | --- | --- |
| Anger | 46.2963 | 51.8519 | 55.5556 | 9.2593 | 3.7037 | 3.7037 |
| Disgust | 68.5185 | 55.5556 | 66.6667 | -1.8519 | 11.1111 | -1.8519 |
| Fear | 65.7407 | 61.1111 | 81.4815 | 15.7407 | 20.3704 | 15.7407 |
| Happiness | 91.6667 | 100.0000 | 100.0000 | 8.3333 | 0.0000 | 0.0000 |
| Neutral | 75.0000 | 94.4444 | 94.4444 | 19.4444 | 0.0000 | 0.0000 |
| Sadness | 81.4815 | 88.8889 | 92.5926 | 11.1111 | 3.7037 | 3.7037 |
| Surprise | 80.5556 | 96.2963 | 80.5556 | 0.0000 | -15.7407 | -15.7407 |

Recall uses native modality units: FEA 54 reenactments per class; Image/Multimodal 108 views per class.
All differences use unrounded counts. The submitted anger gain of 3.71 pp follows subtraction of displayed recalls (55.56 − 51.85); the count-based difference is 3.7037 pp, which rounds to 3.70 pp.

## Dominant dynamic multimodal confusions

| source | target | count | share_of_all_errors_percent |
| --- | --- | --- | --- |
| Anger | Disgust | 44 | 31.6547 |
| Disgust | Happiness | 20 | 14.3885 |
| Surprise | Fear | 20 | 14.3885 |

The three named confusions account for 84/139 = 60.43% of multimodal errors.

## Static–dynamic unimodal complementarity

| group | Dynamic | Static | Dynamic_minus_Static |
| --- | --- | --- | --- |
| both_correct | 476 | 414 | 62 |
| image_only_correct | 74 | 114 | -40 |
| fea_only_correct | 116 | 128 | -12 |
| both_wrong | 90 | 100 | -10 |

Exactly-one-correct cases: 242 → 190.

## Inputs and numerical exports

| setting | path | sha256 |
| --- | --- | --- |
| Static | /workspace/repos/emohevrdb-dfer/4_static_facial_expression_recognition/static_test_predictions.csv | b4536fc35d0d0150d46d50586d36f48e9c33ee2c3d0c9135b8987f73a95501e0 |
| Dynamic | /workspace/repos/emohevrdb-dfer/5_dynamic_facial_expression_recognition/dynamic_test_predictions.csv | ac322c3232bd9a8bcb46f1be049233c2260b3193ebd19197c421ea372e007cde |

- [dynamic_fusion_correctness_groups.csv](tables/dynamic_fusion_correctness_groups.csv)
- [dynamic_class_metrics.csv](tables/dynamic_class_metrics.csv)
- [dynamic_class_recall_comparison.csv](tables/dynamic_class_recall_comparison.csv)
- [dynamic_multimodal_error_pairs.csv](tables/dynamic_multimodal_error_pairs.csv)
- [dominant_multimodal_confusions.csv](tables/dominant_multimodal_confusions.csv)
- [static_dynamic_unimodal_overlap.csv](tables/static_dynamic_unimodal_overlap.csv)

## Interpretation

These are descriptive comparisons of fitted models on the held-out test set. Paired views and repeated FEA decisions are dependent.
Prediction-selection coverage is not a strict fusion ceiling. Conditional fusion outcomes do not establish causal modality selection.
Significance tests, raw FEA patterns, and human annotation agreement are separate analyses.
