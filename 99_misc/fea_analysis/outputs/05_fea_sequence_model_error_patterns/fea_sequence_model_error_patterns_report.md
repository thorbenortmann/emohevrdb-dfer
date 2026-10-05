# FEA sequence model error patterns in the raw FEA signals

## Scope

This analysis compares the raw 30-step sequence-mean FEA profiles of correctly and incorrectly classified reenactments for the final FEA sequence model.

Only the held-out test set is used.

- Test reenactments: 378
- Correctly classified: 296
- Misclassified: 82
- Accuracy: 0.7831
- FEA channels: 63
- Manuscript-relevant mapped individual FEA channels: 35

The analysis is descriptive. Correct–Incorrect differences are not model-reliance or causal-importance measures.

## Correct and incorrect reenactments by ground-truth category

| true_label | Correct | Incorrect |
| --- | --- | --- |
| Anger | 28 | 26 |
| Disgust | 30 | 24 |
| Fear | 33 | 21 |
| Happiness | 54 | 0 |
| Neutral | 51 | 3 |
| Sadness | 48 | 6 |
| Surprise | 52 | 2 |

A category with no misclassified reenactments has no Incorrect raw-signal profile. Missing values are intentionally retained rather than replaced with zero.

## Most common FEA sequence model errors

| true_label | fea_pred | count |
| --- | --- | --- |
| Anger | Disgust | 23 |
| Disgust | Happiness | 10 |
| Fear | Surprise | 8 |
| Disgust | Fear | 7 |
| Fear | Neutral | 6 |
| Fear | Happiness | 4 |
| Sadness | Disgust | 4 |
| Fear | Disgust | 3 |
| Anger | Neutral | 2 |
| Disgust | Anger | 2 |
| Disgust | Sadness | 2 |
| Disgust | Surprise | 2 |
| Neutral | Happiness | 2 |
| Anger | Fear | 1 |
| Disgust | Neutral | 1 |

These counts provide context for the Correct–Incorrect FEA comparisons. The heatmaps themselves remain grouped by **ground-truth category**.

## Primary raw-signal visualizations

### All 63 FEA channels

- `all_63_feas_correct_raw.png`
- `all_63_feas_incorrect_raw.png`
- `all_63_feas_incorrect_minus_correct_raw.png`

The Correct and Incorrect heatmaps use an identical raw-value scale.

### Individual FEAs corresponding to manuscript-relevant AUs

- `paper_relevant_feas_correct_raw.png`
- `paper_relevant_feas_incorrect_raw.png`
- `paper_relevant_feas_incorrect_minus_correct_raw.png`

These focused figures preserve all 35 individual FEA channels corresponding to the 17 manuscript AUs with a dedicated semantic FEA mapping. Left/right and multi-component channels are not averaged together.

## Strongest Correct–Incorrect differences among all FEAs

The values below compare sequence-mean coefficients within the same ground-truth category.

`raw Δ` is the raw Meta coefficient difference:

Incorrect minus Correct.

`SD-scaled Δ` divides that raw difference by the test-set standard deviation of the corresponding reenactment-level FEA summary and is used only to rank channels with different marginal scales.

- **Anger:** LipTightenerR (raw Δ=-0.117, SD-scaled Δ=-2.06; lower in Incorrect); LipTightenerL (raw Δ=-0.116, SD-scaled Δ=-1.97; lower in Incorrect); NoseWrinklerL (raw Δ=+0.263, SD-scaled Δ=+1.53; higher in Incorrect); NoseWrinklerR (raw Δ=+0.266, SD-scaled Δ=+1.52; higher in Incorrect); CheekPuffR (raw Δ=-0.015, SD-scaled Δ=-1.41; lower in Incorrect)
- **Disgust:** NoseWrinklerR (raw Δ=-0.347, SD-scaled Δ=-1.98; lower in Incorrect); NoseWrinklerL (raw Δ=-0.335, SD-scaled Δ=-1.94; lower in Incorrect); BrowLowererR (raw Δ=-0.166, SD-scaled Δ=-1.18; lower in Incorrect); MouthRight (raw Δ=-0.008, SD-scaled Δ=-1.14; lower in Incorrect); BrowLowererL (raw Δ=-0.159, SD-scaled Δ=-1.09; lower in Incorrect)
- **Fear:** UpperLidRaiserR (raw Δ=-0.297, SD-scaled Δ=-1.38; lower in Incorrect); UpperLidRaiserL (raw Δ=-0.197, SD-scaled Δ=-1.10; lower in Incorrect); OuterBrowRaiserL (raw Δ=-0.153, SD-scaled Δ=-0.97; lower in Incorrect); OuterBrowRaiserR (raw Δ=-0.155, SD-scaled Δ=-0.97; lower in Incorrect); InnerBrowRaiserL (raw Δ=-0.128, SD-scaled Δ=-0.84; lower in Incorrect)
- **Happiness:** no misclassified test reenactments; no Correct–Incorrect signal comparison is defined.
- **Neutral:** EyesLookLeftR (raw Δ=-0.104, SD-scaled Δ=-0.97; lower in Incorrect); EyesLookLeftL (raw Δ=-0.072, SD-scaled Δ=-0.89; lower in Incorrect); LidTightenerR (raw Δ=+0.127, SD-scaled Δ=+0.68; higher in Incorrect); LidTightenerL (raw Δ=+0.093, SD-scaled Δ=+0.52; higher in Incorrect); EyesLookUpL (raw Δ=-0.049, SD-scaled Δ=-0.47; lower in Incorrect)
- **Sadness:** EyesClosedL (raw Δ=+0.488, SD-scaled Δ=+4.50; higher in Incorrect); EyesClosedR (raw Δ=+0.462, SD-scaled Δ=+4.37; higher in Incorrect); LipPressorR (raw Δ=+0.186, SD-scaled Δ=+4.16; higher in Incorrect); LipPressorL (raw Δ=+0.182, SD-scaled Δ=+4.12; higher in Incorrect); BrowLowererR (raw Δ=+0.363, SD-scaled Δ=+2.57; higher in Incorrect)
- **Surprise:** LipFunnelerLT (raw Δ=+0.157, SD-scaled Δ=+3.88; higher in Incorrect); LipFunnelerRT (raw Δ=+0.157, SD-scaled Δ=+3.87; higher in Incorrect); LipPuckerR (raw Δ=+0.285, SD-scaled Δ=+2.66; higher in Incorrect); LipPuckerL (raw Δ=+0.279, SD-scaled Δ=+2.58; higher in Incorrect); CheekPuffR (raw Δ=+0.024, SD-scaled Δ=+2.30; higher in Incorrect)

## Interpretation

A negative difference means that a coefficient is weaker on average among misclassified reenactments of that true category. A positive difference means that it is stronger.

These differences can identify signal characteristics associated with successful or unsuccessful recognition. For example, if a category's most characteristic FEA channels are systematically weaker among its errors, that would suggest that the misclassified reenactments contain a less pronounced version of the dataset-level category pattern.

Conversely, if misclassified reenactments show stronger coefficients associated with another category, that may motivate a targeted confusion analysis.

However, the present analysis cannot establish that the FEA sequence model actually depends on those coefficients. That question requires the separate model-perturbation analysis.

## Sample-size caution

Correct and Incorrect groups are not equally sized. Some expression categories have only a small number of model errors, and a category may have no errors at all.

Therefore:

- always report the group sizes shown in the heatmap row labels;
- interpret small Incorrect groups cautiously;
- do not infer statistical significance from visual differences;
- consult the directed confusion analysis below, including its sample and participant counts.

## Recommended figure use

The focused raw heatmaps for the 35 individual FEAs corresponding to the manuscript-relevant AUs are the most compact error-analysis figures for potential use in the paper or supplement.

The complete 63-channel Correct, Incorrect, and difference heatmaps should be retained in the supplementary analysis for transparency.

The difference heatmaps are particularly useful for analysis because they directly show the direction and magnitude of Correct–Incorrect signal changes, but the paired Correct/Incorrect raw heatmaps remain easier to interpret on the original Meta coefficient scale.


## Directed confusion analysis

Only test reenactments are used; sequence means, raw coefficients, and sample weighting are retained. Trajectories are deferred.

| class_a | class_b | errors_both_directions |
| --- | --- | --- |
| Anger | Disgust | 25 |
| Fear | Surprise | 9 |
| Disgust | Happiness | 10 |
| Disgust | Fear | 10 |
| Disgust | Sadness | 6 |
| Fear | Neutral | 6 |

The pair list includes the requested pairs and the five most frequent unordered error pairs, with ties. Results are exploratory; selection and rankings do not constitute statistical tests.

### Reference definitions

Primary: A→B versus correctly classified A. All-A and all-B references and correctly classified B are also exported. All-A contains A→B, so these are overlapping descriptive references, not independent groups.

Raw plots use [0,1]; signed plots share one symmetric scale. Gray rows are unavailable. SD-scaled differences use the full-test sequence-summary SD, not a within-pair pooled SD. Semantic group means are not validated AU measurements.

### Anger versus Disgust

| subset | n | participants |
| --- | --- | --- |
| Anger: all | 54 | 8 |
| Anger: correct | 28 | 6 |
| Anger → Disgust | 23 | 5 |
| Disgust: all | 54 | 8 |
| Disgust: correct | 30 | 7 |
| Disgust → Anger | 2 | 2 |

Figures: `confusion_pairs/Anger__Disgust_paper_35_raw.png`, `Anger__Disgust_all_63_raw.png`, `Anger__Disgust_au_groups_raw.png`; corresponding `_delta.png` files show directed contrasts. `confusion_pairs/Anger__Disgust_sample_distributions.png` shows individual samples colored by participant. PDF versions are also saved.

Largest correct-class mean contrasts (B minus A):

| feature | a_mean | b_mean | raw_delta_b_minus_a | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU23 | 0.1282 | 0.0114 | -0.1167 | -2.0233 |
| AU9 | 0.1110 | 0.3925 | 0.2815 | 1.6191 |
| AU20 | 0.0113 | 0.1289 | 0.1175 | 1.0624 |
| AU10 | 0.1581 | 0.3538 | 0.1958 | 1.0449 |
| AU16 | 0.0060 | 0.1049 | 0.0989 | 0.8374 |

Most similar correct-class group means:

| feature | a_mean | b_mean | a_sd | b_sd | raw_delta_b_minus_a |
| --- | --- | --- | --- | --- | --- |
| AU1 | 0.0419 | 0.0384 | 0.0373 | 0.0393 | -0.0035 |
| AU5 | 0.1153 | 0.1105 | 0.1264 | 0.1264 | -0.0049 |
| AU12 | 0.0508 | 0.0635 | 0.0726 | 0.0820 | 0.0128 |
| AU28 | 0.1003 | 0.0932 | 0.0924 | 0.0578 | -0.0071 |
| AU2 | 0.0240 | 0.0443 | 0.0305 | 0.0377 | 0.0204 |

Similar means do not establish distributional equivalence; consult sample distributions and the exported SDs and quartiles.

#### Anger → Disgust: 23/54 source-class samples (42.6%), 5 participants

The largest participant contribution is 9/23 error samples. Small or concentrated groups should be interpreted as case descriptions, not stable class effects.

Largest individual-channel changes, ranked by absolute SD-scaled difference:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta | shared_participants | within_participant_delta |
| --- | --- | --- | --- | --- | --- | --- |
| LipTightenerR | 0.0103 | 0.1272 | -0.1169 | -2.0636 | 3.0000 | 0.0045 |
| LipTightenerL | 0.0125 | 0.1292 | -0.1167 | -1.9802 | 3.0000 | 0.0061 |
| NoseWrinklerL | 0.4166 | 0.1112 | 0.3054 | 1.7692 | 3.0000 | 0.1743 |
| NoseWrinklerR | 0.4183 | 0.1108 | 0.3075 | 1.7552 | 3.0000 | 0.1749 |
| CheekPuffR | 0.0009 | 0.0160 | -0.0151 | -1.4212 | 3.0000 | -0.0010 |

Largest semantic AU-related group changes:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU23 | 0.0114 | 0.1282 | -0.1168 | -2.0244 |
| AU9 | 0.4174 | 0.1110 | 0.3065 | 1.7629 |
| AU10 | 0.3800 | 0.1581 | 0.2219 | 1.1844 |
| AU24 | 0.0526 | 0.0061 | 0.0465 | 1.0460 |
| AU4 | 0.2909 | 0.1543 | 0.1366 | 0.9564 |

- AU23 · Lip Tightener: errors average 0.011, versus 0.128 for correct Anger and 0.011 for correct Disgust. The absolute gap to the target reference is smaller (0.117 → 0.000). This is a channel-specific descriptive comparison.

- AU9 · Nose Wrinkler: errors average 0.417, versus 0.111 for correct Anger and 0.392 for correct Disgust. The absolute gap to the target reference is smaller (0.281 → 0.025). This is a channel-specific descriptive comparison.

- AU10 · Upper Lip Raiser: errors average 0.380, versus 0.158 for correct Anger and 0.354 for correct Disgust. The absolute gap to the target reference is smaller (0.196 → 0.026). This is a channel-specific descriptive comparison.

Same-participant sensitivity: 3 participants supply both error and correct-source samples. The CSV includes their individual differences and positive/negative direction counts. A missing estimate means no shared participant; differing signs can reflect composition and weighting and must not be ignored.

#### Disgust → Anger: 2/54 source-class samples (3.7%), 2 participants

The largest participant contribution is 1/2 error samples. Small or concentrated groups should be interpreted as case descriptions, not stable class effects.

Largest individual-channel changes, ranked by absolute SD-scaled difference:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta | shared_participants | within_participant_delta |
| --- | --- | --- | --- | --- | --- | --- |
| CheekPuffL | 0.0363 | 0.0012 | 0.0351 | 3.6898 | 2.0000 | 0.0355 |
| CheekPuffR | 0.0362 | 0.0016 | 0.0347 | 3.2584 | 2.0000 | 0.0355 |
| NoseWrinklerR | 0.1798 | 0.3950 | -0.2152 | -1.2282 | 2.0000 | -0.1940 |
| NoseWrinklerL | 0.1873 | 0.3899 | -0.2026 | -1.1738 | 2.0000 | -0.1988 |
| MouthRight | 0.0010 | 0.0093 | -0.0083 | -1.1464 | 2.0000 | -0.0022 |

Largest semantic AU-related group changes:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU9 | 0.1835 | 0.3925 | -0.2089 | -1.2017 |
| AU20 | 0.0230 | 0.1289 | -0.1058 | -0.9565 |
| AU17 | 0.3357 | 0.1836 | 0.1521 | 0.7824 |
| AU16 | 0.0135 | 0.1049 | -0.0914 | -0.7736 |
| AU10 | 0.2104 | 0.3538 | -0.1435 | -0.7657 |

- AU9 · Nose Wrinkler: errors average 0.184, versus 0.392 for correct Disgust and 0.111 for correct Anger. The absolute gap to the target reference is smaller (0.281 → 0.073). This is a channel-specific descriptive comparison.

- AU20 · Lip Stretcher: errors average 0.023, versus 0.129 for correct Disgust and 0.011 for correct Anger. The absolute gap to the target reference is smaller (0.118 → 0.012). This is a channel-specific descriptive comparison.

- AU17 · Chin Raiser: errors average 0.336, versus 0.184 for correct Disgust and 0.342 for correct Anger. The absolute gap to the target reference is smaller (0.158 → 0.006). This is a channel-specific descriptive comparison.

Same-participant sensitivity: 2 participants supply both error and correct-source samples. The CSV includes their individual differences and positive/negative direction counts. A missing estimate means no shared participant; differing signs can reflect composition and weighting and must not be ignored.

### Fear versus Surprise

| subset | n | participants |
| --- | --- | --- |
| Fear: all | 54 | 8 |
| Fear: correct | 33 | 6 |
| Fear → Surprise | 8 | 3 |
| Surprise: all | 54 | 8 |
| Surprise: correct | 52 | 8 |
| Surprise → Fear | 1 | 1 |

Figures: `confusion_pairs/Fear__Surprise_paper_35_raw.png`, `Fear__Surprise_all_63_raw.png`, `Fear__Surprise_au_groups_raw.png`; corresponding `_delta.png` files show directed contrasts. `confusion_pairs/Fear__Surprise_sample_distributions.png` shows individual samples colored by participant. PDF versions are also saved.

Largest correct-class mean contrasts (B minus A):

| feature | a_mean | b_mean | raw_delta_b_minus_a | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU8 | 0.0388 | 0.0797 | 0.0409 | 0.9689 |
| AU18 | 0.0040 | 0.0985 | 0.0944 | 0.8781 |
| AU26 | 0.2488 | 0.3964 | 0.1476 | 0.8265 |
| AU20 | 0.0794 | 0.0099 | -0.0695 | -0.6281 |
| AU22 | 0.0002 | 0.0221 | 0.0219 | 0.5199 |

Most similar correct-class group means:

| feature | a_mean | b_mean | a_sd | b_sd | raw_delta_b_minus_a |
| --- | --- | --- | --- | --- | --- |
| AU17 | 0.0263 | 0.0269 | 0.0335 | 0.0376 | 0.0006 |
| AU9 | 0.0040 | 0.0030 | 0.0150 | 0.0052 | -0.0009 |
| AU6 | 0.0580 | 0.0567 | 0.0884 | 0.0709 | -0.0013 |
| AU28 | 0.0292 | 0.0245 | 0.0238 | 0.0292 | -0.0047 |
| AU12 | 0.0366 | 0.0214 | 0.0733 | 0.0489 | -0.0153 |

Similar means do not establish distributional equivalence; consult sample distributions and the exported SDs and quartiles.

#### Fear → Surprise: 8/54 source-class samples (14.8%), 3 participants

The largest participant contribution is 5/8 error samples. Small or concentrated groups should be interpreted as case descriptions, not stable class effects.

Largest individual-channel changes, ranked by absolute SD-scaled difference:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta | shared_participants | within_participant_delta |
| --- | --- | --- | --- | --- | --- | --- |
| UpperLidRaiserR | 0.1184 | 0.3954 | -0.2770 | -1.2875 | 1.0000 | -0.2442 |
| UpperLidRaiserL | 0.0944 | 0.2983 | -0.2039 | -1.1396 | 1.0000 | -0.1726 |
| UpperLipRaiserR | 0.2093 | 0.1016 | 0.1076 | 0.5610 | 1.0000 | -0.0211 |
| EyesLookRightR | 0.0118 | 0.0490 | -0.0372 | -0.5604 | 1.0000 | -0.0467 |
| EyesLookUpL | 0.0016 | 0.0519 | -0.0503 | -0.4851 | 1.0000 | -0.0720 |

Largest semantic AU-related group changes:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU5 | 0.1064 | 0.3469 | -0.2405 | -1.2834 |
| AU10 | 0.1936 | 0.0983 | 0.0952 | 0.5083 |
| AU2 | 0.1881 | 0.2556 | -0.0675 | -0.4274 |
| AU7 | 0.1375 | 0.0724 | 0.0651 | 0.3706 |
| AU14 | 0.1124 | 0.0753 | 0.0371 | 0.3253 |

- AU5 · Upper Lid Raiser: errors average 0.106, versus 0.347 for correct Fear and 0.311 for correct Surprise. The absolute gap to the target reference is larger (0.035 → 0.205). This is a channel-specific descriptive comparison.

- AU10 · Upper Lip Raiser: errors average 0.194, versus 0.098 for correct Fear and 0.043 for correct Surprise. The absolute gap to the target reference is larger (0.056 → 0.151). This is a channel-specific descriptive comparison.

- AU2 · Outer Brow Raiser: errors average 0.188, versus 0.256 for correct Fear and 0.318 for correct Surprise. The absolute gap to the target reference is larger (0.062 → 0.129). This is a channel-specific descriptive comparison.

Same-participant sensitivity: 1 participants supply both error and correct-source samples. The CSV includes their individual differences and positive/negative direction counts. A missing estimate means no shared participant; differing signs can reflect composition and weighting and must not be ignored.

#### Surprise → Fear: 1/54 source-class samples (1.9%), 1 participants

The largest participant contribution is 1/1 error samples. Small or concentrated groups should be interpreted as case descriptions, not stable class effects.

Largest individual-channel changes, ranked by absolute SD-scaled difference:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta | shared_participants | within_participant_delta |
| --- | --- | --- | --- | --- | --- | --- |
| OuterBrowRaiserR | 0.0018 | 0.3227 | -0.3210 | -2.0034 | 1.0000 | -0.0208 |
| InnerBrowRaiserL | 0.0000 | 0.3060 | -0.3060 | -1.9929 | 1.0000 | -0.0175 |
| OuterBrowRaiserL | 0.0003 | 0.3123 | -0.3120 | -1.9894 | 1.0000 | -0.0180 |
| InnerBrowRaiserR | 0.0005 | 0.3112 | -0.3107 | -1.9769 | 1.0000 | -0.0188 |
| UpperLidRaiserR | 0.0000 | 0.3533 | -0.3533 | -1.6419 | 1.0000 | -0.0009 |

Largest semantic AU-related group changes:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU2 | 0.0010 | 0.3175 | -0.3165 | -2.0024 |
| AU1 | 0.0003 | 0.3086 | -0.3084 | -1.9892 |
| AU5 | 0.0000 | 0.3115 | -0.3115 | -1.6622 |
| AU16 | 0.1442 | 0.0150 | 0.1293 | 1.0941 |
| AU26 | 0.3124 | 0.3964 | -0.0840 | -0.4702 |

- AU2 · Outer Brow Raiser: errors average 0.001, versus 0.318 for correct Surprise and 0.256 for correct Fear. The absolute gap to the target reference is larger (0.062 → 0.255). This is a channel-specific descriptive comparison.

- AU1 · Inner Brow Raiser: errors average 0.000, versus 0.309 for correct Surprise and 0.248 for correct Fear. The absolute gap to the target reference is larger (0.060 → 0.248). This is a channel-specific descriptive comparison.

- AU5 · Upper Lid Raiser: errors average 0.000, versus 0.311 for correct Surprise and 0.347 for correct Fear. The absolute gap to the target reference is larger (0.035 → 0.347). This is a channel-specific descriptive comparison.

Same-participant sensitivity: 1 participants supply both error and correct-source samples. The CSV includes their individual differences and positive/negative direction counts. A missing estimate means no shared participant; differing signs can reflect composition and weighting and must not be ignored.

### Disgust versus Happiness

| subset | n | participants |
| --- | --- | --- |
| Disgust: all | 54 | 8 |
| Disgust: correct | 30 | 7 |
| Disgust → Happiness | 10 | 3 |
| Happiness: all | 54 | 8 |
| Happiness: correct | 54 | 8 |
| Happiness → Disgust | 0 | 0 |

Figures: `confusion_pairs/Disgust__Happiness_paper_35_raw.png`, `Disgust__Happiness_all_63_raw.png`, `Disgust__Happiness_au_groups_raw.png`; corresponding `_delta.png` files show directed contrasts. `confusion_pairs/Disgust__Happiness_sample_distributions.png` shows individual samples colored by participant. PDF versions are also saved.

Largest correct-class mean contrasts (B minus A):

| feature | a_mean | b_mean | raw_delta_b_minus_a | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU12 | 0.0635 | 0.5713 | 0.5077 | 2.2243 |
| AU9 | 0.3925 | 0.0065 | -0.3860 | -2.2202 |
| AU4 | 0.2672 | 0.0354 | -0.2318 | -1.6236 |
| AU14 | 0.0821 | 0.2628 | 0.1807 | 1.5843 |
| AU28 | 0.0932 | 0.1744 | 0.0812 | 1.0030 |

Most similar correct-class group means:

| feature | a_mean | b_mean | a_sd | b_sd | raw_delta_b_minus_a |
| --- | --- | --- | --- | --- | --- |
| AU20 | 0.1289 | 0.1298 | 0.1794 | 0.1511 | 0.0010 |
| AU1 | 0.0384 | 0.0428 | 0.0393 | 0.0391 | 0.0044 |
| AU26 | 0.0797 | 0.0862 | 0.0829 | 0.1011 | 0.0066 |
| AU22 | 0.0022 | 0.0003 | 0.0078 | 0.0006 | -0.0019 |
| AU2 | 0.0443 | 0.0517 | 0.0377 | 0.0511 | 0.0074 |

Similar means do not establish distributional equivalence; consult sample distributions and the exported SDs and quartiles.

#### Disgust → Happiness: 10/54 source-class samples (18.5%), 3 participants

The largest participant contribution is 5/10 error samples. Small or concentrated groups should be interpreted as case descriptions, not stable class effects.

Largest individual-channel changes, ranked by absolute SD-scaled difference:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta | shared_participants | within_participant_delta |
| --- | --- | --- | --- | --- | --- | --- |
| NoseWrinklerR | 0.0621 | 0.3950 | -0.3329 | -1.9002 | 3.0000 | -0.1686 |
| NoseWrinklerL | 0.0760 | 0.3899 | -0.3139 | -1.8183 | 3.0000 | -0.1640 |
| LipCornerPullerL | 0.3904 | 0.0632 | 0.3272 | 1.4494 | 3.0000 | 0.2259 |
| DimplerL | 0.2472 | 0.0821 | 0.1651 | 1.4435 | 3.0000 | 0.1493 |
| LipCornerPullerR | 0.3946 | 0.0638 | 0.3308 | 1.4328 | 3.0000 | 0.2237 |

Largest semantic AU-related group changes:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU9 | 0.0690 | 0.3925 | -0.3234 | -1.8603 |
| AU12 | 0.3925 | 0.0635 | 0.3290 | 1.4412 |
| AU14 | 0.2449 | 0.0821 | 0.1628 | 1.4274 |
| AU6 | 0.5134 | 0.2884 | 0.2250 | 1.0718 |
| AU28 | 0.1599 | 0.0932 | 0.0667 | 0.8241 |

- AU9 · Nose Wrinkler: errors average 0.069, versus 0.392 for correct Disgust and 0.006 for correct Happiness. The absolute gap to the target reference is smaller (0.386 → 0.063). This is a channel-specific descriptive comparison.

- AU12 · Lip Corner Puller: errors average 0.392, versus 0.064 for correct Disgust and 0.571 for correct Happiness. The absolute gap to the target reference is smaller (0.508 → 0.179). This is a channel-specific descriptive comparison.

- AU14 · Dimpler: errors average 0.245, versus 0.082 for correct Disgust and 0.263 for correct Happiness. The absolute gap to the target reference is smaller (0.181 → 0.018). This is a channel-specific descriptive comparison.

Same-participant sensitivity: 3 participants supply both error and correct-source samples. The CSV includes their individual differences and positive/negative direction counts. A missing estimate means no shared participant; differing signs can reflect composition and weighting and must not be ignored.

#### Happiness → Disgust: 0/54 source-class samples (0.0%), 0 participants

No observed errors in this direction; no error profile or contrast is estimated.

### Disgust versus Fear

| subset | n | participants |
| --- | --- | --- |
| Disgust: all | 54 | 8 |
| Disgust: correct | 30 | 7 |
| Disgust → Fear | 7 | 2 |
| Fear: all | 54 | 8 |
| Fear: correct | 33 | 6 |
| Fear → Disgust | 3 | 2 |

Figures: `confusion_pairs/Disgust__Fear_paper_35_raw.png`, `Disgust__Fear_all_63_raw.png`, `Disgust__Fear_au_groups_raw.png`; corresponding `_delta.png` files show directed contrasts. `confusion_pairs/Disgust__Fear_sample_distributions.png` shows individual samples colored by participant. PDF versions are also saved.

Largest correct-class mean contrasts (B minus A):

| feature | a_mean | b_mean | raw_delta_b_minus_a | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU9 | 0.3925 | 0.0040 | -0.3885 | -2.2346 |
| AU4 | 0.2672 | 0.0451 | -0.2221 | -1.5554 |
| AU7 | 0.3322 | 0.0724 | -0.2597 | -1.4786 |
| AU10 | 0.3538 | 0.0983 | -0.2555 | -1.3637 |
| AU1 | 0.0384 | 0.2483 | 0.2099 | 1.3537 |

Most similar correct-class group means:

| feature | a_mean | b_mean | a_sd | b_sd | raw_delta_b_minus_a |
| --- | --- | --- | --- | --- | --- |
| AU22 | 0.0022 | 0.0002 | 0.0078 | 0.0006 | -0.0021 |
| AU14 | 0.0821 | 0.0753 | 0.0626 | 0.1045 | -0.0068 |
| AU12 | 0.0635 | 0.0366 | 0.0820 | 0.0733 | -0.0269 |
| AU23 | 0.0114 | 0.0014 | 0.0274 | 0.0062 | -0.0100 |
| AU8 | 0.0468 | 0.0388 | 0.0602 | 0.0310 | -0.0080 |

Similar means do not establish distributional equivalence; consult sample distributions and the exported SDs and quartiles.

#### Disgust → Fear: 7/54 source-class samples (13.0%), 2 participants

The largest participant contribution is 6/7 error samples. Small or concentrated groups should be interpreted as case descriptions, not stable class effects.

Largest individual-channel changes, ranked by absolute SD-scaled difference:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta | shared_participants | within_participant_delta |
| --- | --- | --- | --- | --- | --- | --- |
| NoseWrinklerL | 0.0191 | 0.3899 | -0.3708 | -2.1481 | 1.0000 | -0.1639 |
| NoseWrinklerR | 0.0189 | 0.3950 | -0.3761 | -2.1466 | 1.0000 | -0.1679 |
| LidTightenerR | 0.0192 | 0.3341 | -0.3149 | -1.6748 | 1.0000 | -0.2581 |
| BrowLowererL | 0.0335 | 0.2743 | -0.2408 | -1.6477 | 1.0000 | -0.1737 |
| BrowLowererR | 0.0301 | 0.2601 | -0.2300 | -1.6289 | 1.0000 | -0.2240 |

Largest semantic AU-related group changes:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU9 | 0.0190 | 0.3925 | -0.3735 | -2.1482 |
| AU4 | 0.0318 | 0.2672 | -0.2354 | -1.6488 |
| AU7 | 0.0464 | 0.3322 | -0.2857 | -1.6267 |
| AU10 | 0.1142 | 0.3538 | -0.2397 | -1.2793 |
| AU16 | 0.2515 | 0.1049 | 0.1465 | 1.2401 |

- AU9 · Nose Wrinkler: errors average 0.019, versus 0.392 for correct Disgust and 0.004 for correct Fear. The absolute gap to the target reference is smaller (0.388 → 0.015). This is a channel-specific descriptive comparison.

- AU4 · Brow Lowerer: errors average 0.032, versus 0.267 for correct Disgust and 0.045 for correct Fear. The absolute gap to the target reference is smaller (0.222 → 0.013). This is a channel-specific descriptive comparison.

- AU7 · Lid Tightener: errors average 0.046, versus 0.332 for correct Disgust and 0.072 for correct Fear. The absolute gap to the target reference is smaller (0.260 → 0.026). This is a channel-specific descriptive comparison.

Same-participant sensitivity: 1 participants supply both error and correct-source samples. The CSV includes their individual differences and positive/negative direction counts. A missing estimate means no shared participant; differing signs can reflect composition and weighting and must not be ignored.

#### Fear → Disgust: 3/54 source-class samples (5.6%), 2 participants

The largest participant contribution is 2/3 error samples. Small or concentrated groups should be interpreted as case descriptions, not stable class effects.

Largest individual-channel changes, ranked by absolute SD-scaled difference:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta | shared_participants | within_participant_delta |
| --- | --- | --- | --- | --- | --- | --- |
| MouthLeft | 0.0602 | 0.0014 | 0.0588 | 4.9250 | 1.0000 | -0.0001 |
| LidTightenerR | 0.4107 | 0.0862 | 0.3246 | 1.7262 | 1.0000 | 0.0881 |
| LidTightenerL | 0.3632 | 0.0587 | 0.3045 | 1.6919 | 1.0000 | 0.0221 |
| BrowLowererL | 0.2523 | 0.0435 | 0.2089 | 1.4290 | 1.0000 | 0.1816 |
| BrowLowererR | 0.2346 | 0.0467 | 0.1878 | 1.3303 | 1.0000 | 0.1385 |

Largest semantic AU-related group changes:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU7 | 0.3870 | 0.0724 | 0.3145 | 1.7906 |
| AU4 | 0.2434 | 0.0451 | 0.1983 | 1.3892 |
| AU5 | 0.1241 | 0.3469 | -0.2228 | -1.1887 |
| AU2 | 0.0730 | 0.2556 | -0.1826 | -1.1552 |
| AU10 | 0.2505 | 0.0983 | 0.1521 | 0.8120 |

- AU7 · Lid Tightener: errors average 0.387, versus 0.072 for correct Fear and 0.332 for correct Disgust. The absolute gap to the target reference is smaller (0.260 → 0.055). This is a channel-specific descriptive comparison.

- AU4 · Brow Lowerer: errors average 0.243, versus 0.045 for correct Fear and 0.267 for correct Disgust. The absolute gap to the target reference is smaller (0.222 → 0.024). This is a channel-specific descriptive comparison.

- AU5 · Upper Lid Raiser: errors average 0.124, versus 0.347 for correct Fear and 0.110 for correct Disgust. The absolute gap to the target reference is smaller (0.236 → 0.014). This is a channel-specific descriptive comparison.

Same-participant sensitivity: 1 participants supply both error and correct-source samples. The CSV includes their individual differences and positive/negative direction counts. A missing estimate means no shared participant; differing signs can reflect composition and weighting and must not be ignored.

### Disgust versus Sadness

| subset | n | participants |
| --- | --- | --- |
| Disgust: all | 54 | 8 |
| Disgust: correct | 30 | 7 |
| Disgust → Sadness | 2 | 2 |
| Sadness: all | 54 | 8 |
| Sadness: correct | 48 | 8 |
| Sadness → Disgust | 4 | 1 |

Figures: `confusion_pairs/Disgust__Sadness_paper_35_raw.png`, `Disgust__Sadness_all_63_raw.png`, `Disgust__Sadness_au_groups_raw.png`; corresponding `_delta.png` files show directed contrasts. `confusion_pairs/Disgust__Sadness_sample_distributions.png` shows individual samples colored by participant. PDF versions are also saved.

Largest correct-class mean contrasts (B minus A):

| feature | a_mean | b_mean | raw_delta_b_minus_a | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU9 | 0.3925 | 0.0220 | -0.3704 | -2.1308 |
| AU15 | 0.1292 | 0.4245 | 0.2953 | 1.8003 |
| AU10 | 0.3538 | 0.0374 | -0.3165 | -1.6892 |
| AU22 | 0.0022 | 0.0580 | 0.0558 | 1.3250 |
| AU17 | 0.1836 | 0.4317 | 0.2481 | 1.2760 |

Most similar correct-class group means:

| feature | a_mean | b_mean | a_sd | b_sd | raw_delta_b_minus_a |
| --- | --- | --- | --- | --- | --- |
| AU18 | 0.0616 | 0.0563 | 0.1257 | 0.0482 | -0.0053 |
| AU2 | 0.0443 | 0.0334 | 0.0377 | 0.0466 | -0.0110 |
| AU12 | 0.0635 | 0.0230 | 0.0820 | 0.0641 | -0.0405 |
| AU1 | 0.0384 | 0.0681 | 0.0393 | 0.0750 | 0.0297 |
| AU5 | 0.1105 | 0.0732 | 0.1264 | 0.1260 | -0.0372 |

Similar means do not establish distributional equivalence; consult sample distributions and the exported SDs and quartiles.

#### Disgust → Sadness: 2/54 source-class samples (3.7%), 2 participants

The largest participant contribution is 1/2 error samples. Small or concentrated groups should be interpreted as case descriptions, not stable class effects.

Largest individual-channel changes, ranked by absolute SD-scaled difference:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta | shared_participants | within_participant_delta |
| --- | --- | --- | --- | --- | --- | --- |
| NoseWrinklerL | 0.0043 | 0.3899 | -0.3856 | -2.2339 | 1.0000 | -0.3421 |
| NoseWrinklerR | 0.0066 | 0.3950 | -0.3884 | -2.2167 | 1.0000 | -0.3568 |
| UpperLipRaiserR | 0.0014 | 0.3639 | -0.3625 | -1.8891 | 1.0000 | -0.3032 |
| UpperLipRaiserL | 0.0040 | 0.3438 | -0.3399 | -1.8533 | 1.0000 | -0.2964 |
| BrowLowererR | 0.0159 | 0.2601 | -0.2441 | -1.7291 | 1.0000 | -0.1635 |

Largest semantic AU-related group changes:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU9 | 0.0054 | 0.3925 | -0.3870 | -2.2261 |
| AU10 | 0.0027 | 0.3538 | -0.3512 | -1.8743 |
| AU4 | 0.0236 | 0.2672 | -0.2436 | -1.7061 |
| AU6 | 0.0282 | 0.2884 | -0.2602 | -1.2396 |
| AU8 | 0.0923 | 0.0468 | 0.0455 | 1.0785 |

- AU9 · Nose Wrinkler: errors average 0.005, versus 0.392 for correct Disgust and 0.022 for correct Sadness. The absolute gap to the target reference is smaller (0.370 → 0.017). This is a channel-specific descriptive comparison.

- AU10 · Upper Lip Raiser: errors average 0.003, versus 0.354 for correct Disgust and 0.037 for correct Sadness. The absolute gap to the target reference is smaller (0.316 → 0.035). This is a channel-specific descriptive comparison.

- AU4 · Brow Lowerer: errors average 0.024, versus 0.267 for correct Disgust and 0.105 for correct Sadness. The absolute gap to the target reference is smaller (0.162 → 0.082). This is a channel-specific descriptive comparison.

Same-participant sensitivity: 1 participants supply both error and correct-source samples. The CSV includes their individual differences and positive/negative direction counts. A missing estimate means no shared participant; differing signs can reflect composition and weighting and must not be ignored.

#### Sadness → Disgust: 4/54 source-class samples (7.4%), 1 participants

The largest participant contribution is 4/4 error samples. Small or concentrated groups should be interpreted as case descriptions, not stable class effects.

Largest individual-channel changes, ranked by absolute SD-scaled difference:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta | shared_participants | within_participant_delta |
| --- | --- | --- | --- | --- | --- | --- |
| EyesClosedL | 0.7453 | 0.0482 | 0.6971 | 6.4327 | 1.0000 | 0.3517 |
| LipPressorR | 0.2817 | 0.0021 | 0.2796 | 6.2653 | 1.0000 | 0.2358 |
| EyesClosedR | 0.7138 | 0.0538 | 0.6601 | 6.2551 | 1.0000 | 0.3290 |
| LipPressorL | 0.2800 | 0.0044 | 0.2757 | 6.2220 | 1.0000 | 0.2339 |
| BrowLowererR | 0.6885 | 0.0972 | 0.5914 | 4.1882 | 1.0000 | 0.3631 |

Largest semantic AU-related group changes:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU43 | 0.7296 | 0.0510 | 0.6786 | 6.4938 |
| AU24 | 0.2809 | 0.0032 | 0.2777 | 6.2448 |
| AU4 | 0.6897 | 0.1052 | 0.5846 | 4.0945 |
| AU18 | 0.3802 | 0.0563 | 0.3239 | 3.0122 |
| AU9 | 0.4624 | 0.0220 | 0.4404 | 2.5334 |

- AU43 · Eyes Closed: errors average 0.730, versus 0.051 for correct Sadness and 0.107 for correct Disgust. The absolute gap to the target reference is larger (0.056 → 0.623). This is a channel-specific descriptive comparison.

- AU24 · Lip Pressor: errors average 0.281, versus 0.003 for correct Sadness and 0.032 for correct Disgust. The absolute gap to the target reference is larger (0.028 → 0.249). This is a channel-specific descriptive comparison.

- AU4 · Brow Lowerer: errors average 0.690, versus 0.105 for correct Sadness and 0.267 for correct Disgust. The absolute gap to the target reference is larger (0.162 → 0.423). This is a channel-specific descriptive comparison.

Same-participant sensitivity: 1 participants supply both error and correct-source samples. The CSV includes their individual differences and positive/negative direction counts. A missing estimate means no shared participant; differing signs can reflect composition and weighting and must not be ignored.

### Fear versus Neutral

| subset | n | participants |
| --- | --- | --- |
| Fear: all | 54 | 8 |
| Fear: correct | 33 | 6 |
| Fear → Neutral | 6 | 3 |
| Neutral: all | 54 | 8 |
| Neutral: correct | 51 | 8 |
| Neutral → Fear | 0 | 0 |

Figures: `confusion_pairs/Fear__Neutral_paper_35_raw.png`, `Fear__Neutral_all_63_raw.png`, `Fear__Neutral_au_groups_raw.png`; corresponding `_delta.png` files show directed contrasts. `confusion_pairs/Fear__Neutral_sample_distributions.png` shows individual samples colored by participant. PDF versions are also saved.

Largest correct-class mean contrasts (B minus A):

| feature | a_mean | b_mean | raw_delta_b_minus_a | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU2 | 0.2556 | 0.0203 | -0.2353 | -1.4890 |
| AU5 | 0.3469 | 0.0693 | -0.2776 | -1.4812 |
| AU1 | 0.2483 | 0.0275 | -0.2208 | -1.4242 |
| AU26 | 0.2488 | 0.0265 | -0.2224 | -1.2454 |
| AU20 | 0.0794 | 0.0055 | -0.0740 | -0.6685 |

Most similar correct-class group means:

| feature | a_mean | b_mean | a_sd | b_sd | raw_delta_b_minus_a |
| --- | --- | --- | --- | --- | --- |
| AU7 | 0.0724 | 0.0726 | 0.1134 | 0.0967 | 0.0002 |
| AU24 | 0.0001 | 0.0000 | 0.0004 | 0.0002 | -0.0001 |
| AU22 | 0.0002 | 0.0003 | 0.0006 | 0.0009 | 0.0001 |
| AU23 | 0.0014 | 0.0006 | 0.0062 | 0.0023 | -0.0008 |
| AU9 | 0.0040 | 0.0013 | 0.0150 | 0.0041 | -0.0026 |

Similar means do not establish distributional equivalence; consult sample distributions and the exported SDs and quartiles.

#### Fear → Neutral: 6/54 source-class samples (11.1%), 3 participants

The largest participant contribution is 4/6 error samples. Small or concentrated groups should be interpreted as case descriptions, not stable class effects.

Largest individual-channel changes, ranked by absolute SD-scaled difference:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta | shared_participants | within_participant_delta |
| --- | --- | --- | --- | --- | --- | --- |
| InnerBrowRaiserR | 0.0110 | 0.2541 | -0.2431 | -1.5470 | 1.0000 | -0.1325 |
| InnerBrowRaiserL | 0.0081 | 0.2424 | -0.2344 | -1.5263 | 1.0000 | -0.1355 |
| UpperLidRaiserR | 0.0696 | 0.3954 | -0.3258 | -1.5144 | 1.0000 | 0.0194 |
| OuterBrowRaiserR | 0.0197 | 0.2609 | -0.2412 | -1.5056 | 1.0000 | -0.1302 |
| OuterBrowRaiserL | 0.0215 | 0.2503 | -0.2288 | -1.4593 | 1.0000 | -0.1597 |

Largest semantic AU-related group changes:

| feature | error_mean | reference_mean | raw_delta | sd_scaled_delta |
| --- | --- | --- | --- | --- |
| AU1 | 0.0095 | 0.2483 | -0.2388 | -1.5402 |
| AU2 | 0.0206 | 0.2556 | -0.2350 | -1.4871 |
| AU5 | 0.0857 | 0.3469 | -0.2612 | -1.3937 |
| AU26 | 0.0407 | 0.2488 | -0.2081 | -1.1654 |
| AU20 | 0.0070 | 0.0794 | -0.0724 | -0.6544 |

- AU1 · Inner Brow Raiser: errors average 0.010, versus 0.248 for correct Fear and 0.027 for correct Neutral. The absolute gap to the target reference is smaller (0.221 → 0.018). This is a channel-specific descriptive comparison.

- AU2 · Outer Brow Raiser: errors average 0.021, versus 0.256 for correct Fear and 0.020 for correct Neutral. The absolute gap to the target reference is smaller (0.235 → 0.000). This is a channel-specific descriptive comparison.

- AU5 · Upper Lid Raiser: errors average 0.086, versus 0.347 for correct Fear and 0.069 for correct Neutral. The absolute gap to the target reference is smaller (0.278 → 0.016). This is a channel-specific descriptive comparison.

Same-participant sensitivity: 1 participants supply both error and correct-source samples. The CSV includes their individual differences and positive/negative direction counts. A missing estimate means no shared participant; differing signs can reflect composition and weighting and must not be ignored.

#### Neutral → Fear: 0/54 source-class samples (0.0%), 0 participants

No observed errors in this direction; no error profile or contrast is estimated.

### Interpretation boundaries and complete outputs

Correct-only and all-class references, all individual-channel and AU-related group contrasts, SDs/quartiles, participant counts, and identifiers of the confused reenactments are exported under `confusion_pairs/`. Files: `raw_profiles_and_distributions.csv`, `all_directed_contrasts.csv`, `class_reference_differences.csv`, `participant_counts.csv`, `confused_sample_sequence_means.csv`.

These comparisons describe signals associated with observed errors. They do not demonstrate causation, model reliance, statistical significance, binary AU presence, or internal emotional states. Sample means can conceal multimodality and participant-specific patterns. Temporal information is deliberately omitted; no claims about temporal phases or trajectories are made.