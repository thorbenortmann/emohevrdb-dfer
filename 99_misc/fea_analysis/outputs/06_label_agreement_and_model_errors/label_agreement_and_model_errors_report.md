# Annotation agreement and dynamic model errors

## Scope

The analysis compares human annotation agreement with the final dynamic Image, FEA, and Multimodal model predictions on the held-out test set.

Primary evaluation units:

- Image: 756 view-level predictions from 378 reenactments.
- FEA: 378 reenactment-level predictions.
- Multimodal: 756 view-level predictions from 378 reenactments.
- Test participants: 8.

The Image and Multimodal view rows are not independent reenactments. Participant-cluster analyses keep both views together.

The three human raters judged one selected central-view reference image. Agreement therefore characterizes perceived category agreement on that image, not objective correctness of the full sequence, side view, or FEA signal.

## Agreement across all retained SFEA/DFEA samples

The independently read SFEA and DFEA memberships match exactly: 1727 shared reenactments across train, validation, and test.

| category | n_2_of_3 | n_3_of_3 | n_total | percent_2_of_3 | percent_3_of_3 |
| --- | --- | --- | --- | --- | --- |
| Anger | 76 | 99 | 175 | 43.4286 | 56.5714 |
| Disgust | 95 | 116 | 211 | 45.0237 | 54.9763 |
| Fear | 129 | 85 | 214 | 60.2804 | 39.7196 |
| Happiness | 9 | 291 | 300 | 3.0000 | 97.0000 |
| Neutral | 37 | 269 | 306 | 12.0915 | 87.9085 |
| Sadness | 62 | 178 | 240 | 25.8333 | 74.1667 |
| Surprise | 76 | 205 | 281 | 27.0463 | 72.9537 |
| Total | 484 | 1243 | 1727 | 28.0255 | 71.9745 |

Split totals:

| split | n_2_of_3 | n_3_of_3 | n_total | percent_2_of_3 | percent_3_of_3 |
| --- | --- | --- | --- | --- | --- |
| train | 272 | 692 | 964 | 28.2158 | 71.7842 |
| validation | 109 | 276 | 385 | 28.3117 | 71.6883 |
| test | 103 | 275 | 378 | 27.2487 | 72.7513 |

These counts describe the retained dataset and are independent of model predictions.

## Class-level agreement and model recall

| category | all_dataset_percent_3_of_3 | test_percent_3_of_3 | image_recall | fea_recall | multimodal_recall |
| --- | --- | --- | --- | --- | --- |
| Anger | 56.5714 | 74.0741 | 0.4630 | 0.5185 | 0.5556 |
| Disgust | 54.9763 | 51.8519 | 0.6852 | 0.5741 | 0.6667 |
| Fear | 39.7196 | 35.1852 | 0.6574 | 0.5926 | 0.8148 |
| Happiness | 97.0000 | 100.0000 | 0.9167 | 1.0000 | 1.0000 |
| Neutral | 87.9085 | 87.0370 | 0.7500 | 0.9259 | 0.9444 |
| Sadness | 74.1667 | 87.0370 | 0.8148 | 0.9074 | 0.9259 |
| Surprise | 72.9537 | 74.0741 | 0.8056 | 0.9630 | 0.8056 |

Descriptive correlations across the seven classes:

| modality | agreement_scope | n_classes | pearson_r | spearman_rho |
| --- | --- | --- | --- | --- |
| Image | all retained splits | 7 | 0.7131 | 0.7857 |
| Image | test split | 7 | 0.5125 | 0.7638 |
| FEA | all retained splits | 7 | 0.8704 | 0.7500 |
| FEA | test split | 7 | 0.7491 | 0.6547 |
| Multimodal | all retained splits | 7 | 0.7050 | 0.7500 |
| Multimodal | test split | 7 | 0.5244 | 0.7092 |

## Main findings

### Class-level recognition difficulty broadly mirrors human annotation agreement

The class-level pattern is consistent across all three modalities. **Happiness** has the highest unanimous annotation agreement across the retained dataset (**97.0% 3/3**) and also shows very high test recall: **91.7% for Image**, **100.0% for FEA**, and **100.0% for Multimodal FER**.

At the other end, **Fear (39.7% 3/3), Disgust (55.0%), and Anger (56.6%)** have the lowest unanimous-agreement rates. These categories also tend to be among the more difficult recognition classes, although the relationship is not perfectly monotonic. Fear is the clearest counterexample: despite the lowest annotation agreement, Multimodal recall reaches **81.5%**, indicating that multimodal information can partly compensate for a category that is comparatively ambiguous in the human reference-image annotations.

Across the seven categories, the descriptive Pearson correlation between unanimous agreement across all retained splits and test recall is **r = 0.713 for Image**, **r = 0.870 for FEA**, and **r = 0.705 for Multimodal FER**. The corresponding Spearman correlations are **ρ = 0.786**, **0.750**, and **0.750**. Because these correlations are based on only seven expression categories, they are treated as descriptive summaries rather than inferential evidence.

**References:** `classwise_agreement_and_model_recall.csv`, `classwise_agreement_recall_correlations.csv`, and the three `*_class_agreement_vs_recall.png` figures.

### The raw 2/3-versus-3/3 performance gap is substantial, but class composition matters

Using the primary evaluation units, accuracy rises from **59.7% to 77.6% for Image FER (+17.9 pp)**, from **66.0% to 82.9% for FEA FER (+16.9 pp)**, and from **69.9% to 86.0% for Multimodal FER (+16.1 pp)**.

However, the 2/3 and 3/3 subsets have different class compositions; most notably, Happiness is absent from the 2/3 test subset. After averaging recall equally across the classes represented in both groups, the 3/3-minus-2/3 difference is **14.8 pp for Image**, only **1.9 pp for FEA**, and **9.9 pp for Multimodal FER**.

The FEA result is particularly important: its raw agreement gap is large, but it almost disappears after equal class weighting. This indicates that much of the raw FEA gap is attributable to **which expression categories occur in the 2/3 and 3/3 subsets**, rather than to a uniform within-category agreement effect. A more substantial class-standardized association remains for Image and Multimodal FER.

**References:** `overall_metrics_by_modality_and_agreement.csv`, `class_standardized_accuracy_by_modality.csv`, and the three `*_per_class_recall_contrasts.csv` tables.

### Errors on ambiguous samples frequently match the dissenting human label

The strongest cross-modal result is the correspondence between model errors and the dissenting rater on 2/3-agreement samples. Among such errors, the predicted category equals the dissenting human label for **44/83 Image errors (53.0%)**, **26/35 FEA errors (74.3%)**, and **49/62 Multimodal errors (79.0%)**.

These observed rates are higher than the corresponding class-conditioned shuffle means of **39.0% for Image**, **45.0% for FEA**, and **50.1% for Multimodal FER**.

Thus, many errors are not arbitrary alternative categories: they coincide with the **same alternative interpretation chosen by the dissenting human rater**. This supports the interpretation that a substantial subset of model errors occurs on category boundaries that were also ambiguous to human annotators. It does **not** establish that the model prediction or the dissenting annotation is objectively correct, nor does it justify relabeling the benchmark.

**References:** `minority_label_correspondence_by_modality.csv`, `minority_match_descriptive_benchmark_by_modality.csv`, and `all_directed_confusions_by_modality_and_agreement.csv`.

### The Image and Multimodal findings are not driven by one camera perspective

Central and Side views show very similar 2/3-versus-3/3 accuracy patterns. For Image FER, accuracy is **59.2% vs. 78.2%** for Central and **60.2% vs. 77.1%** for Side. For Multimodal FER, the corresponding values are **69.9% vs. 86.2%** for Central and **69.9% vs. 85.8%** for Side.

Minority-label correspondence among 2/3 errors is likewise present in both perspectives: **47.6% Central vs. 58.5% Side for Image**, and **77.4% vs. 80.6% for Multimodal FER**.

This supports using both views in the primary Image and Multimodal evaluation rather than interpreting the agreement association as a Central-view-only artifact.

**Reference:** `image_multimodal_view_sensitivity_summary.csv`.

### Participant-level sensitivity reinforces the modality-specific nuance

When Participant × Class cells containing both agreement levels are weighted equally, the mean 3/3-minus-2/3 accuracy contrast is **16.25 pp for Image**, **-1.58 pp for FEA**, and **13.25 pp for Multimodal FER**. This again shows that the FEA agreement contrast is small after conditioning more closely on participant and class, whereas Image and Multimodal retain larger differences.

Participant-cluster bootstrap intervals are reported as an exploratory uncertainty analysis because only 8 independent test participants are available. They should not be treated as definitive inferential tests.

**References:** `participant_class_sensitivity_summary.csv`, `participant_cluster_bootstrap_by_modality.csv`, and `leave_one_participant_out_by_modality.csv`.

### Overall interpretation

Taken together, the analyses support two complementary conclusions. First, **class-level recognition difficulty broadly mirrors human annotation ambiguity across Image, FEA, and Multimodal FER**, which is consistent with the hardest categories reflecting properties of the underlying expression/category structure rather than a failure confined to one modality. Second, the sample-level 2/3-versus-3/3 association is modality-dependent: it is largely explained by class composition for FEA, while clearer within-class differences remain for Image and Multimodal FER.

The most consistent result across all three modalities is that **errors on 2/3-agreement samples frequently select exactly the dissenting rater's alternative category**. This provides direct descriptive evidence that many model errors coincide with category ambiguity already visible in human perception of the retained reference images.


## Detailed performance tables

### Performance by annotation-agreement group

| modality | agreement | n | accuracy | macro_f1 | weighted_f1 | macro_f1_common_labels |
| --- | --- | --- | --- | --- | --- | --- |
| Image | 2/3 | 206 | 0.5971 | 0.5206 | 0.6272 | 0.6073 |
| Image | 3/3 | 550 | 0.7764 | 0.7544 | 0.7823 | 0.7302 |
| FEA | 2/3 | 103 | 0.6602 | 0.5951 | 0.6650 | 0.6943 |
| FEA | 3/3 | 275 | 0.8291 | 0.7904 | 0.8298 | 0.7721 |
| Multimodal | 2/3 | 206 | 0.6990 | 0.6244 | 0.7152 | 0.7285 |
| Multimodal | 3/3 | 550 | 0.8600 | 0.8350 | 0.8621 | 0.8223 |

### Class-standardized accuracy

| modality | shared_classes | classes | accuracy_2_of_3 | accuracy_3_of_3 | difference_3_minus_2_pp |
| --- | --- | --- | --- | --- | --- |
| Image | 6 | Anger \| Disgust \| Fear \| Neutral \| Sadness \| Surprise | 0.5831 | 0.7307 | 14.7660 |
| FEA | 6 | Anger \| Disgust \| Fear \| Neutral \| Sadness \| Surprise | 0.7319 | 0.7509 | 1.8992 |
| Multimodal | 6 | Anger \| Disgust \| Fear \| Neutral \| Sadness \| Surprise | 0.7101 | 0.8089 | 9.8807 |

### Dissenting-rater correspondence among 2/3 errors

| modality | analysis_unit | two_vote_rows | two_vote_errors | minority_matches | observed_match_rate_among_errors | class_conditioned_shuffle_mean | shuffle_q025 | shuffle_q975 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Image | view | 206 | 83 | 44 | 0.5301 | 0.3905 | 0.3133 | 0.4699 |
| FEA | reenactment | 103 | 35 | 26 | 0.7429 | 0.4498 | 0.3143 | 0.5714 |
| Multimodal | view | 206 | 62 | 49 | 0.7903 | 0.5009 | 0.4032 | 0.6129 |

### Central-versus-Side sensitivity

Overall accuracy by view and agreement group:

| modality | perspective | agreement | n | accuracy |
| --- | --- | --- | --- | --- |
| Image | Central | 2/3 | 103 | 0.5922 |
| Image | Central | 3/3 | 275 | 0.7818 |
| Image | Side | 2/3 | 103 | 0.6019 |
| Image | Side | 3/3 | 275 | 0.7709 |
| Multimodal | Central | 2/3 | 103 | 0.6990 |
| Multimodal | Central | 3/3 | 275 | 0.8618 |
| Multimodal | Side | 2/3 | 103 | 0.6990 |
| Multimodal | Side | 3/3 | 275 | 0.8582 |

Minority-label correspondence among 2/3 errors by view:

| modality | perspective | n | minority_match_rate_among_errors |
| --- | --- | --- | --- |
| Image | Central | 42 | 0.4762 |
| Image | Side | 41 | 0.5854 |
| Multimodal | Central | 31 | 0.7742 |
| Multimodal | Side | 31 | 0.8065 |

### Participant sensitivity and uncertainty

Participant × Class equal-cell summary:

| modality | shared_participant_class_cells | participants_represented | mean_equal_cell_difference_3_minus_2_pp |
| --- | --- | --- | --- |
| Image | 32 | 8 | 16.2463 |
| FEA | 32 | 8 | -1.5848 |
| Multimodal | 32 | 8 | 13.2478 |

Participant-cluster bootstrap intervals for accuracy and class-standardized accuracy:

| modality | metric | difference_3_minus_2 | ci025 | ci975 | valid_bootstrap_draws |
| --- | --- | --- | --- | --- | --- |
| Image | accuracy | 0.1793 | -0.0385 | 0.3882 | 2000 |
| Image | class_standardized_accuracy | 0.1477 | -0.0220 | 0.3217 | 1955 |
| FEA | accuracy | 0.1689 | -0.0029 | 0.3587 | 2000 |
| FEA | class_standardized_accuracy | 0.0190 | -0.0627 | 0.0979 | 1955 |
| Multimodal | accuracy | 0.1610 | 0.0071 | 0.2977 | 2000 |
| Multimodal | class_standardized_accuracy | 0.0988 | 0.0049 | 0.1815 | 1955 |

## Interpretation boundaries

- Annotation disagreement is not proof of label error.
- Human ratings concern one central-view reference image, not the full dynamic signal.
- Image and Multimodal pooled-view percentages use 756 view rows, but those rows represent 378 paired reenactments.
- No view-level independence is assumed in participant-cluster uncertainty analyses.
- No labels are changed.
- No model is retrained.
- No new test-set tuning is performed.
- Minority-label correspondence does not establish model correctness.
- Class-level correlations across seven categories are descriptive only.
