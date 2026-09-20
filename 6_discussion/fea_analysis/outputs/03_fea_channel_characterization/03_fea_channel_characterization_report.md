# Point 3 — DFEA channel characterization

## Scope

- DFEA observations: 51,810
- Reenactments: 1,727
- Participants: 36
- FEA channels: 63
- Splits: train, validation, test
- Sequence length: 30 observations

The pooled summaries are descriptive and dataset-composition weighted.
Time-step rows from the same reenactment are not treated as statistically independent samples.
No FEA channel is removed at this stage.

## Main empirical findings

### Strong concentration near zero and right-skewed coefficient distributions

For all 63/63 FEA channels, the pooled mean is larger than the pooled median. This is consistent with strongly right-skewed marginal distributions for many channels.

- 45/63 channels have a median <= 0.01.
- 61/63 channels have a median <= 0.05.
- 12/63 channels have at least 80% of observations <= 0.01.

This means that many FEAs are inactive or only weakly expressed for large parts of the dataset while still showing stronger values in a subset of observations.

### Some sparse channels nevertheless show large observed ranges

Low medians must not be interpreted as evidence that a channel is irrelevant. Several channels combine a very low median with a large upper tail. For example, the largest robust P99-P01 ranges occur for the NoseWrinkler and LipCornerPuller channels.

| fea_name | mean | median | std | iqr | p99_p01 | fraction_le_0_01 |
| --- | --- | --- | --- | --- | --- | --- |
| NoseWrinklerR | 0.0786 | 0.0000 | 0.2095 | 0.0108 | 1.0000 | 0.7394 |
| LipCornerPullerR | 0.1099 | 0.0000 | 0.2598 | 0.0278 | 1.0000 | 0.6391 |
| LipCornerPullerL | 0.1071 | 0.0003 | 0.2533 | 0.0278 | 1.0000 | 0.6069 |
| NoseWrinklerL | 0.0786 | 0.0000 | 0.2080 | 0.0119 | 1.0000 | 0.6848 |
| CheekRaiserR | 0.1411 | 0.0380 | 0.2184 | 0.1579 | 0.9291 | 0.2658 |
| CheekRaiserL | 0.1573 | 0.0543 | 0.2251 | 0.1926 | 0.9291 | 0.2247 |
| LipCornerDepressorL | 0.0912 | 0.0086 | 0.2075 | 0.0308 | 0.9019 | 0.5204 |
| BrowLowererL | 0.1237 | 0.0319 | 0.2003 | 0.1503 | 0.8915 | 0.3725 |
| LipCornerDepressorR | 0.0848 | 0.0001 | 0.2023 | 0.0250 | 0.8814 | 0.6385 |
| UpperLidRaiserL | 0.0890 | 0.0000 | 0.1977 | 0.0431 | 0.8775 | 0.6575 |

### Some channels reach or approach the upper coefficient bound

31/63 channels reach approximately 1.0 in at least one observation, and 4/63 have P99 approximately equal to 1.0.

This makes a sequence maximum unsuitable as the primary summary because it can be dominated by one extreme observation and may be affected by coefficient saturation.

### Marginal distributions differ across participant-disjoint splits

16/63 channels have a difference of more than 0.05 between the highest and lowest split-specific mean.

The largest differences are:

| fea_name | train_mean | validation_mean | test_mean | mean_range_across_splits |
| --- | --- | --- | --- | --- |
| BrowLowererL | 0.0991 | 0.2023 | 0.1064 | 0.1032 |
| BrowLowererR | 0.0863 | 0.1777 | 0.0987 | 0.0914 |
| NoseWrinklerL | 0.0548 | 0.1366 | 0.0802 | 0.0818 |
| NoseWrinklerR | 0.0551 | 0.1365 | 0.0795 | 0.0814 |
| UpperLidRaiserR | 0.0792 | 0.1472 | 0.1570 | 0.0778 |
| LidTightenerR | 0.1199 | 0.1500 | 0.1936 | 0.0738 |
| CheekRaiserL | 0.1281 | 0.1958 | 0.1924 | 0.0678 |
| LidTightenerL | 0.1137 | 0.1352 | 0.1781 | 0.0644 |
| InnerBrowRaiserR | 0.0608 | 0.1240 | 0.1039 | 0.0633 |
| LipCornerDepressorL | 0.0731 | 0.1350 | 0.0926 | 0.0619 |

These differences do not by themselves indicate a problem because train, validation, and test contain different participants and the split composition differs. They do mean that important later findings should be checked for qualitative consistency across splits.

## Highest pooled mean coefficients

| fea_name | mean | median | std | p95 | p99 |
| --- | --- | --- | --- | --- | --- |
| CheekRaiserL | 0.1573 | 0.0543 | 0.2251 | 0.6829 | 0.9291 |
| LidTightenerR | 0.1427 | 0.0263 | 0.2079 | 0.6088 | 0.7983 |
| CheekRaiserR | 0.1411 | 0.0380 | 0.2184 | 0.6641 | 0.9291 |
| UpperLipRaiserR | 0.1339 | 0.0172 | 0.2011 | 0.6003 | 0.7833 |
| LidTightenerL | 0.1326 | 0.0266 | 0.1916 | 0.5613 | 0.7537 |
| ChinRaiserT | 0.1324 | 0.0380 | 0.2035 | 0.6019 | 0.8527 |
| UpperLipRaiserL | 0.1291 | 0.0157 | 0.1961 | 0.5830 | 0.7606 |
| BrowLowererL | 0.1237 | 0.0319 | 0.2003 | 0.6093 | 0.8915 |
| EyesLookLeftR | 0.1138 | 0.0626 | 0.1341 | 0.3889 | 0.5025 |
| UpperLidRaiserR | 0.1114 | 0.0000 | 0.2196 | 0.6753 | 0.8620 |

Absolute coefficient magnitude is descriptive only. Because the 63 channels have different marginal distributions, a larger raw mean does not imply that the channel is more category-specific or more important to the classifier.

## Channels with the smallest robust P99-P01 ranges

| fea_name | mean | median | std | iqr | p99_p01 | fraction_le_0_01 |
| --- | --- | --- | --- | --- | --- | --- |
| CheekSuckR | 0.0009 | 0.0000 | 0.0121 | 0.0000 | 0.0172 | 0.9890 |
| CheekSuckL | 0.0009 | 0.0000 | 0.0109 | 0.0000 | 0.0190 | 0.9881 |
| MouthRight | 0.0016 | 0.0000 | 0.0079 | 0.0000 | 0.0268 | 0.9324 |
| MouthLeft | 0.0045 | 0.0000 | 0.0107 | 0.0084 | 0.0371 | 0.7718 |
| CheekPuffL | 0.0039 | 0.0000 | 0.0158 | 0.0000 | 0.0588 | 0.8660 |
| CheekPuffR | 0.0044 | 0.0000 | 0.0158 | 0.0001 | 0.0611 | 0.8521 |
| JawSidewaysLeft | 0.0081 | 0.0000 | 0.0232 | 0.0096 | 0.0968 | 0.7577 |
| JawSidewaysRight | 0.0102 | 0.0024 | 0.0252 | 0.0109 | 0.0977 | 0.6100 |
| LipPressorR | 0.0054 | 0.0000 | 0.0346 | 0.0000 | 0.1580 | 0.9112 |
| LipPressorL | 0.0054 | 0.0000 | 0.0344 | 0.0000 | 0.1585 | 0.9082 |

No feature is removed based on this table. Low marginal variation can still coexist with category-specific or participant-specific information.

## Consequences for sequence aggregation

### Primary aggregation: sequence mean

For every reenactment and FEA, use the mean across the 30 chronological observations as the primary sequence-level summary.

Reasons:

1. it uses all 30 observations;
2. it preserves moderate or sustained activation;
3. unlike the median, it does not collapse many sparse but episodically active channels to approximately zero;
4. unlike the maximum, it is not determined by one isolated observation.

Because every DFEA sequence contains exactly 30 observations, the sequence mean is also the normalized area under the observed 30-step coefficient trajectory.

### Sensitivity aggregation: sequence P90

Also compute the 90th percentile across the 30 observations.

P90 provides a complementary summary for stronger, shorter-lived activation. It is less sensitive to a single extreme observation than the maximum while retaining more information about the upper part of the trajectory than the mean.

A category-associated pattern that is visible under both mean and P90 is robust to this aggregation choice. A pattern that is strong only under P90 should later be inspected in the full timestep 1-30 trajectories.

### Do not use median or maximum as the primary sequence summary

- **Median:** many channels are so sparse that the median is approximately zero and would hide episodic activation.
- **Maximum:** a single observation can dominate the result, and many channels occasionally approach the upper coefficient bound.

Median and maximum may still be retained as diagnostics if useful.

## Consequences for category aggregation

After sequence aggregation, there are two distinct ways to summarize an expression category.

### Sample-weighted / reenactment-weighted profile — primary dataset view

Simply average the sequence summaries across all reenactments of a category. Every reenactment counts once.

This answers:

> What is the average FEA pattern across the reenactments that actually exist in EmoHeVRDB for this category?

A participant with more reenactments therefore contributes more observations. This is not an extra normalization step; it is the ordinary mean over the available samples.

### Participant-balanced profile — robustness view

First average within each Participant x Category combination and then average those participant-level values. Each participant with data for that category therefore receives the same weight.

This answers:

> What is the average category-specific FEA pattern across participants when participants with more reenactments do not dominate the estimate?

The current data contain between 1 and 10 reenactments per observed Participant x Category combination. Missing combinations: participant 22: Fear, participant 26: Sadness.

Therefore participant balancing is useful as a robustness/generalizability check, but it should not replace the primary sample-weighted dataset characterization.

**Important:** participant balancing changes weights; it does not normalize FEA values.

## Participant-specific neutral centering

Neutral centering is a separate operation from participant balancing.

For each participant and FEA, compute the participant's average Neutral sequence summary and subtract it from that participant's other category summaries.

This answers:

> How does the participant's FEA pattern for a category differ from that participant's own neutral baseline?

All 36/36 participants have Neutral reenactments, so participant-specific neutral centering is feasible for the complete participant set.

Use raw coefficients as the primary representation and neutral-centered coefficients as a sensitivity analysis. Do not apply category-wise centering that would remove the category differences of interest.

## Raw scale versus standardized cross-channel comparisons

Raw [0,1] coefficients should always be retained because they preserve the original Meta coefficient scale.

However, the channels have substantially different marginal distributions. When the later goal is to compare which FEAs are relatively elevated for a category, also provide a channel-wise standardized view based on reenactment-level sequence summaries.

Standardization is a comparison/visualization aid; it must not replace the raw-value analysis.

## Planned analysis grid for later steps

The category-level analysis should initially compute all four combinations:

| Sequence summary | Category aggregation | Role |
| --- | --- | --- |
| Mean | Sample-weighted | Primary dataset characterization |
| Mean | Participant-balanced | Robustness across participants |
| P90 | Sample-weighted | Sensitivity to stronger/episodic activation |
| P90 | Participant-balanced | Participant-robust P90 sensitivity |

For Mean and P90, additionally generate participant-specific neutral-centered variants as sensitivity analyses.

The results should be compared before selecting a compact main-paper visualization.

## Split usage

For dataset/signal characterization, train, validation, and test may be combined because the target is the benchmark data rather than held-out model performance. Important patterns should nevertheless be checked separately across the participant-disjoint splits.

Final model evaluation, prediction-error analysis, prediction trajectories, and model-reliance analyses remain test-only.

## Interpretation boundary

The low-/high-value fractions and robust-range statistics characterize proprietary Meta FEA coefficients.

They are not:

- FACS Action Unit occurrence rates,
- validated AU intensities,
- physiological muscle measurements, or
- measures of internal emotional state.

The decisions above are intended to characterize and aggregate the recorded FEA signals without converting them into validated FACS measurements.
