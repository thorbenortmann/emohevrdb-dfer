# Paired Model Accuracy Comparisons

[Discussion](../README.md)

**Table 7 reports seven comparisons.** The repository also includes Static Image–Static FEA and Dynamic Image–Dynamic FEA, giving nine notebooks in total.

- [Static comparisons](static-significance-tests/README.md): notebook/report links for three modality comparisons.
- [Dynamic and static–dynamic comparisons](dynamic-significance-tests/README.md): notebook/report links for six comparisons.
- [Combined results](result-reports/00_summary.md): accuracy differences, confidence intervals, p-values, and supporting counts.

## Shared inputs and regeneration

The notebooks read the shared [static](../../4_static_facial_expression_recognition/static_test_predictions.csv) and/or [dynamic](../../5_dynamic_facial_expression_recognition/dynamic_test_predictions.csv) CSVs without raw datasets or checkpoints. Run them from their containing directories using [the shared setup](../../env/README.md). They export CSVs into local `statistical_results/` directories; Markdown reports are separate saved summaries.

## Methods

Image/Multimodal comparisons average central/side correctness within each of 378 reenactments. Eight repository comparisons use centered paired bootstrap p-values; Static–Dynamic FEA uses exact two-sided McNemar. All confidence intervals are paired percentile-bootstrap intervals (1,000,000 resamples; seed 42).

Primary p-values are nominal, with no joint multiplicity correction. Secondary view-test families use Holm adjustment where applicable. Participant summaries and paired t-tests are descriptive/sensitivity outputs; primary inference does not model dependence between reenactments from the same participant or training variability. [The comparison plan](statistical_comparison_plan.md) gives details.

Sequence-order tests in Section 5 use separate two-test Holm families within each modality.
