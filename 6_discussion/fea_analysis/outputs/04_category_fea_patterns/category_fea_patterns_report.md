# Category-level FEA patterns and FACS-related group summaries

## Analysis scope

This analysis summarizes the 30-step DFEA sequences from all participant-disjoint train, validation, and test splits in order to characterize the recorded FEA signals themselves.

- Reenactments: 1,727
- Participants: 36
- FEA channels: 63
- Semantic FEA groups: 32
- Manuscript AU-related groups with a dedicated FEA correspondence: 17
- Individual FEA channels corresponding to those mapped manuscript AUs: 35

The analysis is descriptive. It does not measure model reliance and does not treat the Meta coefficients as validated FACS Action Unit measurements.

## Sequence aggregation

The **30-step sequence mean** is the primary reenactment-level summary. It uses every observation and is less likely than the sequence median to suppress sparse or episodic activation, while being less sensitive than the maximum to one extreme observation.

The **sequence P90** is retained as a sensitivity summary for stronger or more episodic activation.

## Category aggregation

The primary category profile is **sample-weighted**: every reenactment contributes once.

A **participant-balanced** robustness profile first averages within Participant × Category and then averages participants equally. Participant balancing changes the weighting of the available reenactments; it does not normalize the FEA coefficients.

Participant-specific **Neutral centering** is analyzed separately as a baseline sensitivity analysis.

## Cross-channel comparison

Raw [0,1] coefficient profiles are retained. Because the 63 channels have substantially different marginal distributions, channel-wise standardized reenactment summaries are also used to identify relative category-associated patterns across different FEAs.

A standardized value of, for example, `+1.5` means that the category-level mean lies 1.5 pooled reenactment-level standard deviations above the overall mean of that FEA channel. These values therefore facilitate comparisons between channels but should not be interpreted as Meta coefficient magnitudes or FACS AU intensities.

## Robustness across aggregation choices

| comparison | representation | correlation |
| --- | --- | --- |
| Mean: sample-weighted vs participant-balanced | standardized | 0.9926 |
| P90: sample-weighted vs participant-balanced | standardized | 0.9939 |
| Sample-weighted: Mean vs P90 | standardized | 0.9956 |
| Participant-balanced: Mean vs P90 | standardized | 0.9945 |

The category profiles are highly robust to the main aggregation choices. Correlations between alternative standardized 7 × 63 profiles range from **0.993 to 0.996**.

In particular, the correlation between sample-weighted and participant-balanced sequence-mean profiles is **0.993**, indicating that unequal numbers of reenactments per participant have little influence on the overall category-pattern structure.

Likewise, sequence Mean and sequence P90 produce a correlation of **0.996** under sample weighting. Thus, the principal category-associated patterns are not dependent on whether sustained activation is summarized by the Mean or stronger/shorter activation is emphasized using P90.

These correlations summarize overall matrix similarity only; individual FEAs and categories should still be inspected when the analyses differ.

The corresponding heatmaps are:

- `fea_category_mean_sample_weighted_standardized.png`
- `fea_category_mean_participant_balanced_standardized.png`
- `fea_category_p90_sample_weighted_standardized.png`
- `fea_category_mean_participant_balanced_neutral_standardized.png`

## Split consistency

| split_a | split_b | profile_correlation |
| --- | --- | --- |
| train | validation | 0.8668 |
| train | test | 0.8259 |
| validation | test | 0.8041 |

The standardized category profiles are also positively correlated across the three participant-disjoint splits, with correlations ranging from **0.804 to 0.867**.

These correlations are lower than the correlations between aggregation variants. This is expected because train, validation, and test contain different participants. The results therefore suggest that the broad category-associated FEA structure is reproducible across participant groups while still exhibiting meaningful inter-participant variation.

The split comparisons are descriptive and should not be interpreted as inferential tests.

## Strongest category-associated individual FEAs

Values in parentheses are standardized sequence-mean deviations under the primary sample-weighted analysis.

- **Anger:** BrowLowererR (1.09), BrowLowererL (1.07), LidTightenerL (0.84), ChinRaiserB (0.83), ChinRaiserT (0.83)
- **Disgust:** NoseWrinklerL (1.46), NoseWrinklerR (1.46), BrowLowererL (1.01), BrowLowererR (0.97), LidTightenerL (0.94)
- **Fear:** OuterBrowRaiserR (0.71), UpperLidRaiserR (0.69), OuterBrowRaiserL (0.69), UpperLidRaiserL (0.68), InnerBrowRaiserR (0.65)
- **Happiness:** LipCornerPullerR (1.74), LipCornerPullerL (1.73), DimplerR (1.51), DimplerL (1.48), CheekRaiserR (1.20)
- **Neutral:** EyesLookLeftL (0.07), EyesLookLeftR (0.07), EyesLookUpR (0.06), EyesLookUpL (0.06), EyesLookRightL (-0.07)
- **Sadness:** LipCornerDepressorR (1.69), LipCornerDepressorL (1.68), ChinRaiserB (1.35), ChinRaiserT (1.16), LipFunnelerRB (0.81)
- **Surprise:** JawDrop (1.38), OuterBrowRaiserL (0.94), OuterBrowRaiserR (0.94), JawThrust (0.85), InnerBrowRaiserR (0.75)

The complete pattern is visualized in `fea_category_mean_sample_weighted_standardized.png`. The focused heatmap `paper_au_individual_feas_mean_sample_weighted_standardized.png` shows only the individual FEA channels that correspond to the manuscript-relevant mapped AUs, without averaging left/right or multi-component channels.

## Strongest category-associated semantic FEA groups

Values in parentheses are standardized sequence-mean deviations under the primary sample-weighted analysis.

- **Anger:** AU4 Brow Lowerer (1.08), AU17 Chin Raiser (0.84), AU7 Lid Tightener (0.81), AU9 Nose Wrinkler (0.76), MouthLeft (unmapped) (0.66)
- **Disgust:** AU9 Nose Wrinkler (1.46), AU4 Brow Lowerer (0.99), AU7 Lid Tightener (0.90), AU10 Upper Lip Raiser (0.89), MouthLeft (unmapped) (0.77)
- **Fear:** AU5 Upper Lid Raiser (0.72), AU2 Outer Brow Raiser (0.71), AU1 Inner Brow Raiser (0.62), AU26 Jaw Drop (0.45), AU20 Lip Stretcher (0.26)
- **Happiness:** AU12 Lip Corner Puller (1.74), AU14 Dimpler (1.50), AU6 Cheek Raiser (1.17), AU28 Lip Suck (1.11), AU16 Lower Lip Depressor (0.81)
- **Neutral:** EYE61 Eyes Turn Left (0.07), EYE63 Eyes Up (0.06), EYE62 Eyes Turn Right (-0.08), AD35 Cheek Suck (-0.11), AU24 Lip Pressor (-0.20)
- **Sadness:** AU15 Lip Corner Depressor (1.69), AU17 Chin Raiser (1.27), AU22 Lip Funneler (0.75), AD34 Cheek Puff (0.66), AD30 Jaw Sideways (0.53)
- **Surprise:** AU26 Jaw Drop (1.38), AU2 Outer Brow Raiser (0.94), AD29 Jaw Thrust (0.85), AU1 Inner Brow Raiser (0.74), AU8 Lips Toward Each Other (0.67)

The complete grouped profile is visualized in `semantic_groups_mean_sample_weighted_standardized.png`, while `paper_au_groups_mean_sample_weighted_standardized.png` restricts the visualization to AU-related groups that correspond to AUs used in the manuscript's theoretical FACS table.

## Narrative interpretation of the main category patterns

Several expression categories show pronounced and readily interpretable FEA patterns in the primary standardized sequence-mean analysis.

### Happiness

Happiness shows some of the largest positive standardized deviations observed in the analysis. The strongest individual channels are `LipCornerPullerR` (**1.74 SD**) and `LipCornerPullerL` (**1.73 SD**), followed by `DimplerR` (**1.51 SD**) and `DimplerL` (**1.48 SD**).

At the semantic-group level, the largest deviations are therefore found for **AU12 Lip Corner Puller (1.74 SD)**, **AU14 Dimpler (1.50 SD)**, and **AU6 Cheek Raiser (1.17 SD)**.

The bilateral LipCornerPuller and Dimpler results are also visible in the focused individual-FEA heatmap and are not artifacts of averaging left and right channels into AU-related groups.

### Sadness

Sadness is characterized most strongly by the lip-corner depressor and chin-raiser channels. `LipCornerDepressorR` and `LipCornerDepressorL` reach **1.69 SD** and **1.68 SD**, respectively.

After semantic grouping, **AU15 Lip Corner Depressor** reaches **1.69 SD**, followed by **AU17 Chin Raiser (1.27 SD)**.

This produces a relatively concentrated lower-face pattern compared with categories such as Fear and Surprise.

### Surprise

Surprise shows its strongest individual deviation for `JawDrop` at **1.38 SD**. `OuterBrowRaiserL` and `OuterBrowRaiserR` are both approximately **0.94 SD**, while `InnerBrowRaiserR` reaches **0.75 SD**.

At group level, this corresponds primarily to **AU26 Jaw Drop (1.38 SD)**, **AU2 Outer Brow Raiser (0.94 SD)**, and **AU1 Inner Brow Raiser (0.74 SD)**.

`JawThrust` is additionally elevated at **0.85 SD** and is represented separately as the AD29-related semantic group rather than being merged into an AU-related group.

### Disgust

Disgust is dominated by the bilateral NoseWrinkler channels: `NoseWrinklerL` reaches **1.46 SD** and `NoseWrinklerR` **1.46 SD**.

The corresponding **AU9 Nose Wrinkler** semantic group reaches **1.46 SD**. Additional elevations occur for **AU4 Brow Lowerer (0.99 SD)**, **AU7 Lid Tightener (0.90 SD)**, and **AU10 Upper Lip Raiser (0.89 SD)**.

Thus, Disgust is not represented by a single isolated coefficient but by a broader pattern containing particularly strong nose-wrinkling activation.

### Anger

Anger is characterized most strongly by `BrowLowererR` (**1.09 SD**) and `BrowLowererL` (**1.07 SD**).

At group level, the strongest deviations are **AU4 Brow Lowerer (1.08 SD)**, **AU17 Chin Raiser (0.84 SD)**, and **AU7 Lid Tightener (0.81 SD)**.

Anger and Disgust therefore share elevated BrowLowerer- and LidTightener-related signals. This descriptive overlap is potentially relevant to the later confusion-focused analysis, but the present analysis does not establish that these shared FEA patterns cause classification errors.

### Fear

Fear is dominated by upper-face-related channels. `OuterBrowRaiserR` reaches **0.71 SD**, `OuterBrowRaiserL` **0.69 SD**, `UpperLidRaiserR` **0.69 SD**, and `UpperLidRaiserL` **0.68 SD**.

The strongest semantic groups are **AU5 Upper Lid Raiser (0.72 SD)**, **AU2 Outer Brow Raiser (0.71 SD)**, and **AU1 Inner Brow Raiser (0.62 SD)**.

Compared with the stronger deviations seen for Happiness, Sadness, Disgust, and Surprise, the largest Fear-related standardized deviations are more moderate.

### Neutral

Neutral differs from the posed expression categories in that none of its individual FEAs shows a strong positive standardized deviation. The largest positive values are only `EyesLookLeftL` (**0.07 SD**), `EyesLookLeftR` (**0.07 SD**), `EyesLookUpR` (**0.06 SD**), and `EyesLookUpL` (**0.06 SD**).

This is consistent with the Neutral category remaining close to the pooled mean for most expression-related FEA channels rather than being characterized by one strongly elevated movement.

## Cross-category observations

Three broader observations follow from the category profiles.

First, several categories exhibit **bilateral activation patterns**. Examples include LipCornerPullerL/R for Happiness, LipCornerDepressorL/R for Sadness, NoseWrinklerL/R for Disgust, and OuterBrowRaiserL/R for Fear and Surprise. The focused individual-FEA heatmap is therefore useful alongside the AU-group heatmap because it confirms whether a grouped effect is bilateral or driven primarily by one constituent channel.

Second, some semantic groups are elevated in more than one category. In particular, **AU4 Brow Lowerer** and **AU7 Lid Tightener** are elevated for both Anger and Disgust. Conversely, other patterns are considerably more category-specific in these descriptive profiles, such as AU12-related LipCornerPuller activation for Happiness, AU15-related LipCornerDepressor activation for Sadness, AU9-related NoseWrinkler activation for Disgust, and AU26-related JawDrop activation for Surprise.

Third, the very high similarity between Mean and P90 profiles and between sample-weighted and participant-balanced profiles indicates that these category-associated patterns are not primarily artifacts of one temporal summary or of participants contributing different numbers of reenactments.

These observations motivate the subsequent temporal and confusion-focused analyses. They should not yet be interpreted as evidence that the dynamic classifier relies on the same channels; classifier reliance requires the separate model-perturbation analysis.

## FACS-related grouping

The 63 channels are summarized into 32 semantic groups:

- AU-related groups;
- Action Descriptor-related groups;
- approximate eye-position groups;
- two unmapped channels retained as individual groups.

Group values are means of their member FEA sequence summaries. This is a semantic and visualization aid, not an official Meta-to-FACS conversion.

The manuscript's theoretical FACS table contains 20 unique AUs. Seventeen have a dedicated semantic FEA correspondence in the 63-channel schema. In addition to the AU-group heatmap, the analysis retains the individual FEA channels corresponding to these mapped AUs so that left/right and multi-component differences are not hidden by within-AU averaging.

The three manuscript AUs without a dedicated FEA are:

| au_code | au_name | paper_expression_categories |
| --- | --- | --- |
| AU11 | Nasolabial Deepener | Sadness |
| AU25 | Lips Part | Anger \| Disgust \| Fear \| Sadness |
| AU27 | Mouth Stretch | Fear \| Surprise |

## Interpretation boundaries

The observed patterns should be described as **category-associated FEA patterns**.

They do not establish:

- that the Meta coefficients are validated FACS AU measurements;
- that a positive coefficient corresponds to binary AU occurrence;
- that standardized magnitude represents AU intensity;
- that the listed FEAs are causally important to the classifier; or
- that the observed facial configurations measure participants' internal emotional states.

The semantic AU-related grouping provides an interpretable crosswalk for characterizing the recorded FEA signals. Together with the manuscript-relevant AU-group and individual-FEA views, it provides the descriptive non-temporal comparison with the manuscript's expected FACS configurations. Temporal correspondence and dynamic-model reliance are handled separately.

## Recommended use in subsequent analyses

1. Retain the **sequence Mean + sample-weighted** profile as the primary dataset characterization.
2. Use **participant-balanced** and **P90** profiles as robustness checks rather than replacing the primary view.
3. Use participant-specific **Neutral-centered** profiles as a separate baseline sensitivity analysis.
4. Preserve the complete 63-channel results in the supplementary analysis.
5. Use the semantic FEA groups to improve interpretability, with the 17 manuscript AU-related groups as a compact candidate visualization.
6. Retain the focused individual-FEA heatmap for the FEAs corresponding to those 17 mapped manuscript AUs, because AU-level averaging can hide left/right or component-specific structure.
7. Use the observed Anger–Disgust overlap and the Fear–Surprise similarities as explicit targets for the later confusion-focused trajectory analysis.
8. Treat the present AU-group and manuscript-relevant individual-FEA analyses as the descriptive non-temporal comparison with the manuscript's expected FACS configurations; do not convert them into a binary AU match/no-match score. Temporal correspondence remains for the trajectory analysis.
9. Do not call these patterns model-relevant. Model reliance requires the later dynamic-LSTM perturbation analysis.
