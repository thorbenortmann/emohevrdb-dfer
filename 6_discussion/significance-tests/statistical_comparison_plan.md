# Statistical Comparison Plan

## Goal and Shared Data

Assess whether FER accuracy differs across modalities and between static and dynamic models on the same test data.

The test set contains **378 reenactments from eight participants**. Image and Multimodal models each produce two predictions per reenactment: Central and Side, giving 756 predictions. FEA models produce one prediction per reenactment, repeated in both view rows of the prediction CSVs.

The notebooks check sample IDs, both camera views, consistent ground-truth labels and participant IDs, and identical FEA predictions across duplicated rows. Static–Dynamic comparisons additionally check matching sample sets and metadata. Image/Multimodal predictions are paired by sample ID; FEA predictions are reduced to one per reenactment and paired by reenactment ID.

## General Principles

- **Direction:** for A vs. B, report B − A. Positive differences favor B.
- **Accuracy:** a correct prediction contributes 1; an incorrect prediction contributes 0. For Image/Multimodal, average the two view-correctness values within each reenactment. Averaging these 378 scores reproduces pooled accuracy over 756 predictions. This is not voting or combining predicted classes.
- **Pairing:** keep both views together. The primary resampling unit is the reenactment, not an individual view or participant.
- **Reporting:** report accuracy differences and 95% confidence intervals in percentage points (pp). All tests are two-sided, with nominal α = 0.05.
- **Sensitivity:** all nine notebooks apply a one-sample t-test against zero to the same 378 paired differences (377 degrees of freedom).

## Comparison Types

### 1. FEA vs. Image or Multimodal

Applies separately to Static and Dynamic:

- Image vs. FEA: **FEA − pooled Image**.
- FEA vs. Multimodal: **pooled Multimodal − FEA**.

Each reenactment contributes one binary FEA score and one view-averaged Image/Multimodal score (0, 0.5, or 1). Calculate their paired difference.

**Primary analysis:** centered paired bootstrap for the p-value; ordinary paired percentile bootstrap for the 95% interval, as specified below. A label-swap/sign-flip test is not performed: the binary FEA and view-averaged scores have different supports.

**Sensitivity:** one-sample t-test on the same paired differences.

**Secondary analysis:** three exact McNemar tests, each on 378 paired binary outcomes:

| Main comparison | Secondary comparisons, in notebook order |
| --- | --- |
| Image vs. FEA | Central Image vs. FEA; Side Image vs. FEA; Central Image vs. Side Image |
| FEA vs. Multimodal | FEA vs. Central Multimodal; FEA vs. Side Multimodal; Central Multimodal vs. Side Multimodal |

Differences remain second minus first. Apply Holm correction across the three tests within each notebook. Report raw and adjusted p-values and paired correctness counts. These tests compare individual accuracies; they do not directly test whether the modality effect differs between camera views.

### 2. Image vs. Multimodal

Applies separately to Static and Dynamic. Both models predict the same 756 view samples.

For each reenactment, subtract Image correctness from Multimodal correctness for each view, then average the two differences. The mean of these 378 paired values equals the pooled Multimodal − Image accuracy difference.

**Primary analysis:** centered paired bootstrap for the p-value and ordinary paired percentile bootstrap for the interval.

**Sensitivity:** one-sample t-test on the same differences.

No secondary significance tests are performed. Central and Side accuracies are descriptive.

### 3. Static vs. Dynamic Image or Multimodal

Applies to Image and Multimodal separately. Both settings predict corresponding Central and Side samples from the same 378 reenactments.

Use the procedure in Type 2, with **Dynamic − Static** as the difference: calculate the paired difference for each view and average within reenactment.

**Primary analysis:** centered paired bootstrap for the p-value and ordinary paired percentile bootstrap for the interval.

**Sensitivity:** one-sample t-test on the same differences.

View-specific Static–Dynamic differences are descriptive; no view-specific significance or interaction test is performed.

### 4. Static vs. Dynamic FEA

Both models provide one binary outcome for each of 378 reenactments. Remove duplicated view rows before comparison.

**Primary analysis:** exact two-sided McNemar test, using `mcnemar(table, exact=True, correction=False)`. Report both accuracies, **Dynamic − Static**, and the four paired counts: both correct, Static only correct, Dynamic only correct, and both wrong. The two discordant counts determine the McNemar p-value.

**Effect-size interval:** ordinary paired percentile bootstrap on the 378 Dynamic − Static differences. This notebook calculates no bootstrap p-value; McNemar remains the primary test.

**Sensitivity:** one-sample t-test on the same differences.

## Bootstrap Procedure

All bootstraps use 1,000,000 resamples, batch size 10,000, and `np.random.default_rng(42)`, initialized separately for each function call. Each resample draws 378 reenactments with replacement.

**Confidence interval:** resample the original paired differences and calculate their mean. The 95% interval is the 2.5th to 97.5th percentile of these means (`np.quantile`, default linear interpolation).

**P-value for Types 1–3:** generate a separate set of resamples. Subtract the observed mean difference from each resampled mean to form a distribution centered at zero. Count a draw as extreme when its absolute centered mean is at least as large as the absolute observed difference. With K extreme draws among B = 1,000,000 draws, report **p = (K + 1)/(B + 1)**. The minimum value is 1/1,000,001, not zero.

For reproducible boundary counting, the function doubles the differences (which are −1, −0.5, 0, 0.5, or 1) and uses integer sums. If S is the original sum and S* the resampled sum of these doubled values, count **|S* − S| ≥ |S|**. Equality is included.

Within each batch, interval draws precede separate null-test draws from the same generator. Types 1–3 therefore use one million draws for the interval plus one million for the test. Type 4 uses only interval draws. Preserve seed, batch size, row order, and draw order to reproduce the simulation.

## Participant-Level Heterogeneity

For each of eight participants, report reenactment count, both accuracies, and their difference. Summarize participants favoring each condition, ties, and the median participant difference.

This is descriptive. Primary estimates weight reenactments equally. No participant-level significance test or additional clustering of reenactments by participant is implemented; participant tables do not correct that dependence. The analyses also do not measure variability from retraining models.

## Multiplicity and Interpretation

The nine primary p-values have **no joint multiplicity correction**. Their intervals are individual, not simultaneous. Holm correction is limited to four separate families of three secondary tests in Type 1. Sensitivity t-tests are not included in those families.

Use the designated primary test for significance decisions. Nonsignificance does not establish equivalence. Different significance decisions across settings do not establish an interaction.

## Reporting

Organize each result report around the primary comparison, sensitivity test, secondary tests where present, and participant table. Include both accuracies, difference, interval, p-values, and explicit significance decisions.

Also report descriptive correctness overlap: both correct, only A correct, only B correct, and both wrong. Use 756 paired view samples whenever Image/Multimodal is involved (repeating FEA per view), and 378 reenactments for FEA vs. FEA. These counts are calculated from predictions; they are not additional notebook hypothesis tests. Only B correct represents corrections; only A correct represents losses. “Both wrong” need not mean the same incorrect class.

Each notebook exports reenactment data, primary results, sensitivity results, participant results, and a summary to `statistical_results`. Type 1 additionally exports secondary McNemar results. Accuracy fields are proportions; fields marked `pp` are percentage points.
