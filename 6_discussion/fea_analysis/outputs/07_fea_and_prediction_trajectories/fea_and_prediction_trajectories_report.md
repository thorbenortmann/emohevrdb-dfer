# FEA and prediction trajectory analysis

## Scope

The dataset-level FEA trajectory analyses use all **1,727 reenactments** across train, validation, and test. Model-linked analyses use only the **378 held-out test reenactments**.

Prediction trajectories are prefix probes of the frozen trained FEA sequence model. The model is not retrained for individual prefix lengths. Consequently, especially the shortest prefixes should be interpreted as descriptive probes rather than independently validated short-sequence models.

## Main findings

### 1. Category-associated FEA trajectories are robust to participant balancing

The temporal FEA profiles change very little when participants are weighted equally. The correlation between sample-weighted and participant-balanced category trajectories ranges from **r = 0.9950 (Fear)** to **r = 0.9999 (Happiness)**. Mean absolute differences range from **0.0006** to **0.0080**.

See `participant_balanced_trajectory_robustness.csv`.

The strongest standardized manuscript-relevant FEA channel for each category is:

| true_label | fea_name | au_code | au_name | standardized_sequence_mean |
| --- | --- | --- | --- | --- |
| Anger | BrowLowererR | AU4 | Brow Lowerer | 1.0882 |
| Disgust | NoseWrinklerL | AU9 | Nose Wrinkler | 1.4619 |
| Fear | OuterBrowRaiserR | AU2 | Outer Brow Raiser | 0.7140 |
| Happiness | LipCornerPullerR | AU12 | Lip Corner Puller | 1.7416 |
| Neutral | LipPressorR | AU24 | Lip Pressor | -0.1991 |
| Sadness | LipCornerDepressorR | AU15 | Lip Corner Depressor | 1.6943 |
| Surprise | JawDrop | AU26 | Jaw Drop | 1.3844 |

These results describe category-associated Meta FEA patterns and should not be interpreted as validation of the coefficients as FACS AU intensities.

### 2. Category means strongly smooth individual FEA transitions

Individual reenactments commonly contain much sharper FEA transitions than the corresponding category-average trajectories suggest. Among the selected non-Neutral category-associated channels, the median individual maximum positive change is between **3.92×** and **7.78×** the largest positive change visible in the corresponding category mean.

The strongest examples are:

| true_label | fea_name | median_sample_max_positive_step_change | mean_curve_max_positive_step_change | median_to_mean_curve_jump_ratio | median_step_of_max_positive_change | timing_iqr_steps |
| --- | --- | --- | --- | --- | --- | --- |
| Sadness | ChinRaiserB | 0.1730 | 0.0222 | 7.7750 | 14.0000 | 12.0000 |
| Sadness | LipCornerDepressorR | 0.2267 | 0.0292 | 7.7611 | 14.0000 | 11.0000 |
| Sadness | LipCornerDepressorL | 0.2280 | 0.0306 | 7.4501 | 14.0000 | 11.0000 |
| Anger | LidTightenerL | 0.0981 | 0.0133 | 7.3528 | 16.0000 | 15.0000 |
| Surprise | JawDrop | 0.1311 | 0.0217 | 6.0324 | 13.0000 | 12.0000 |
| Disgust | NoseWrinklerL | 0.1330 | 0.0235 | 5.6705 | 16.0000 | 14.0000 |
| Happiness | CheekRaiserR | 0.1215 | 0.0216 | 5.6127 | 15.0000 | 12.0000 |
| Fear | UpperLidRaiserR | 0.0696 | 0.0125 | 5.5643 | 15.0000 | 14.0000 |

The broad timing IQRs additionally show that these strongest FEA changes occur at heterogeneous chronological positions across reenactments. This temporal heterogeneity explains why category-average trajectories can appear gradual even when individual trajectories contain substantially sharper transitions.

See `fea_sample_vs_mean_transition_summary.csv` and the `focused_top_fea_transition_steps_<category>.png` figures.

### 3. Prediction trajectories show the same smoothing effect

Across the held-out test set, the median largest one-step increase in **true-class probability** is **0.198**.

Class-specific comparisons between individual reenactments and category-average curves are:

| true_label | mean_curve_max_true_probability_increase | median_sample_max_true_probability_increase | median_to_mean_curve_jump_ratio | median_step_of_max_true_probability_increase | q25_step_of_max_true_probability_increase | q75_step_of_max_true_probability_increase |
| --- | --- | --- | --- | --- | --- | --- |
| Anger | 0.0301 | 0.2109 | 6.9962 | 15.0000 | 6.0000 | 21.0000 |
| Disgust | 0.0399 | 0.1303 | 3.2668 | 20.0000 | 10.0000 | 24.7500 |
| Fear | 0.0265 | 0.1365 | 5.1549 | 14.5000 | 4.0000 | 22.5000 |
| Happiness | 0.0840 | 0.3547 | 4.2212 | 6.0000 | 2.0000 | 14.5000 |
| Neutral | 0.1095 | 0.1699 | 1.5516 | 2.0000 | 2.0000 | 9.0000 |
| Sadness | 0.0742 | 0.2648 | 3.5696 | 7.0000 | 2.0000 | 18.0000 |
| Surprise | 0.0425 | 0.2196 | 5.1684 | 13.5000 | 5.0000 | 19.7500 |

Thus, smooth mean probability curves should not be interpreted as evidence that individual model decisions evolve equally gradually. Strong probability transitions frequently occur at different sequence positions across reenactments.

See `prediction_sample_vs_mean_transition_summary.csv` and `true_class_probability_jump_step_distribution_min_prefix_1.png`.

### 4. High-confidence predictions are usually persistent once reached

**301 of 378 test reenactments (79.6%)** reach an eventual-final-class probability of at least 0.80 at some point.

Among those reenactments, **89.0%** never fall below 0.80 afterward. The median timestep from which the final predicted class remains unchanged is **step 10.0**.

These results support the observation that many individual prediction trajectories contain a relatively rapid transition followed by a stable high-confidence decision.

See `prediction_high_confidence_and_stability_summary.csv`.

### 5. Correct and incorrect reenactments can now be compared using the same true-class event

The event-alignment analysis centers both correct and incorrect reenactments on their own strongest positive increase in **true-class probability**. Thus, for an Anger reenactment, the reference probability is always the Anger probability regardless of the final predicted class.

A positive true-class probability event is available for **378 of 378 test reenactments (100.0%)**.

The resulting `event_aligned_true_class_fea_correct_vs_incorrect_<category>.png` figures compare the same category-associated FEA channels between successful and unsuccessful recognition. They should be used to assess whether characteristic FEA trajectories differ descriptively between correct and incorrect reenactments rather than mixing both outcomes into one average.

See `true_probability_alignment_sample_counts.csv` and `event_aligned_fea_and_prediction_trajectories.csv`.

### 6. Several FEA transitions occur close to rapid increases in true-class evidence

The temporal-coincidence analysis now uses **true-class probability for both correct and incorrect reenactments**. It measures how closely each selected FEA's strongest positive change occurs to the strongest positive increase in model evidence for the ground-truth class.

The strongest temporal coincidences among correctly classified reenactments are:

| true_label | fea_name | n_reenactments | n_valid_event_distances | median_event_distance | fraction_within_1_step | fraction_within_2_steps | median_change_correlation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Surprise | OuterBrowRaiserL | 52 | 49 | 0.0000 | 0.6327 | 0.7755 | 0.5555 |
| Surprise | OuterBrowRaiserR | 52 | 50 | 0.0000 | 0.6400 | 0.7200 | 0.5362 |
| Surprise | JawDrop | 52 | 52 | -1.0000 | 0.4423 | 0.6731 | 0.4536 |
| Disgust | NoseWrinklerL | 30 | 30 | -1.0000 | 0.4333 | 0.6000 | 0.2997 |
| Happiness | LipCornerPullerR | 54 | 53 | 0.0000 | 0.4717 | 0.5660 | 0.3613 |
| Happiness | LipCornerPullerL | 54 | 53 | 0.0000 | 0.4717 | 0.5472 | 0.3646 |
| Disgust | NoseWrinklerR | 30 | 30 | -1.0000 | 0.4667 | 0.5333 | 0.2920 |
| Anger | BrowLowererL | 28 | 28 | 0.0000 | 0.2857 | 0.5000 | 0.1967 |
| Happiness | CheekRaiserR | 54 | 54 | 2.0000 | 0.4074 | 0.4815 | 0.2862 |
| Disgust | BrowLowererL | 30 | 30 | -0.5000 | 0.3000 | 0.4667 | 0.1521 |
| Anger | BrowLowererR | 28 | 28 | 0.5000 | 0.2857 | 0.4643 | 0.1708 |
| Sadness | ChinRaiserB | 48 | 48 | -1.0000 | 0.3125 | 0.3958 | 0.1597 |

The fractions within ±1 and ±2 steps quantify descriptive temporal proximity only. Likewise, the within-reenactment change correlations describe co-occurrence of FEA and probability changes; neither measure establishes causal model reliance.

See `fea_probability_temporal_coincidence_summary.csv`.

### 7. Directed confusion patterns remain asymmetric

The targeted confusion analysis yields:

| true_class | final_predicted_class | n_errors | fea_groups_shown |
| --- | --- | --- | --- |
| Anger | Disgust | 23 | AU4 · Brow Lowerer \| AU17 · Chin Raiser \| AU9 · Nose Wrinkler |
| Disgust | Anger | 2 | AU9 · Nose Wrinkler \| AU4 · Brow Lowerer \| AU17 · Chin Raiser |
| Fear | Surprise | 8 | AU5 · Upper Lid Raiser \| AU2 · Outer Brow Raiser \| AU26 · Jaw Drop |
| Surprise | Fear | 1 | AU26 · Jaw Drop \| AU2 · Outer Brow Raiser \| AU5 · Upper Lid Raiser |

The corresponding `confusion_synthesis_<source>_to_<target>.png` figures show the evolution of the true and competing class probabilities together with strongly associated semantic AU-related FEA groups.

These analyses characterize the signal patterns accompanying recurrent errors, but they do not establish that individual FEA groups causally determine those errors.

## Overall interpretation

The trajectory analyses indicate that category-associated FEA signals and model probabilities both contain substantially sharper sample-level transitions than their smooth category averages suggest. These transitions occur at heterogeneous chronological positions, making sequence averaging potentially misleading about the underlying temporal dynamics.

Aligning reenactments to their individual true-class probability transitions provides a more interpretable comparison between correctly and incorrectly recognized samples. Several category-associated FEA changes occur close in time to rapid increases in model evidence for the corresponding ground-truth category, but the strength of this association varies across categories and channels.

These results therefore provide descriptive evidence that temporally localized FEA changes and prediction transitions are related. They do **not** demonstrate which FEA channels the LSTM causally relies on. Such a claim requires the separate perturbation or permutation analysis.

## Interpretation boundaries

- Raw FEA values are Meta coefficients, not validated FACS AU intensities.
- Sequence positions are chronological observations, not annotated onset, apex, or offset phases.
- Category-average trajectories can substantially smooth asynchronous individual transitions.
- Prefix predictions use the frozen full-sequence model and are not independently retrained sequence-length models.
- Very short prefixes should therefore be interpreted cautiously.
- Temporal coincidence between FEA and prediction changes does not establish causal feature importance.
