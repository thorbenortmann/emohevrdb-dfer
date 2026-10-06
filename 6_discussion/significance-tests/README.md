# Paired Model Accuracy Comparisons

[Up one level](../README.md) · [Repository README](../../README.md)

Nine comparison notebooks evaluate the fitted static and dynamic models on the same 378 test reenactments from eight participants. **Seven comparisons appear in Table 7**; Static Image–Static FEA and Dynamic Image–Dynamic FEA are additional repository analyses.

## Navigation

- [Static comparisons](static-significance-tests/README.md): three modality comparisons.
- [Dynamic and static–dynamic comparisons](dynamic-significance-tests/README.md): six comparisons.
- [Result reports](result-reports/README.md), including the [combined nine-comparison summary](result-reports/00_summary.md).
- [Statistical comparison plan](statistical_comparison_plan.md): methods and inference scope.

## Shared inputs and regeneration

The notebooks use the shared [Section 4 static CSV](../../4_static_facial_expression_recognition/static_test_predictions.csv) and/or [Section 5 dynamic CSV](../../5_dynamic_facial_expression_recognition/dynamic_test_predictions.csv). Collection and checkpoint setup remain in those sections. The comparison notebooks require no trained models or raw datasets.

Use the [shared environment and execution instructions](../../env/README.md). Each notebook regenerates CSV tables in its containing directory's `statistical_results/` folder. The Markdown result reports are saved written summaries, separate from those numerical exports.

## Methods and evaluation units

Image and Multimodal accuracies use 756 view predictions. The paired bootstrap averages central- and side-view correctness within each reenactment and resamples the 378 paired units. FEA uses one prediction per reenactment.

Eight repository comparisons use a two-sided centered paired bootstrap for the primary p-value. Static–Dynamic FEA uses exact two-sided McNemar. All primary confidence intervals are paired percentile-bootstrap intervals; notebooks use 1,000,000 resamples and seed 42.

Primary p-values are nominal, without joint multiplicity correction. Holm correction applies separately to the secondary view-test families where reported. Participant summaries and paired t-tests are descriptive/sensitivity outputs. The primary analyses do not model dependence among reenactments from the same participant or training variability.

Sequence-order comparisons use separate two-test Holm families in [Section 5](../../5_dynamic_facial_expression_recognition/README.md).
