# Model Significance Tests

[Up one level](../README.md) · [Repository home](../../README.md)

Nine comparisons cover the three static modalities, the three dynamic modalities, and Static–Dynamic changes within each modality.

## Start here

- [Combined results summary](result-reports/00_summary.md): all nine comparisons with links to their individual reports.
- [Statistical comparison plan](statistical_comparison_plan.md): analysis methods and interpretation scope.

## Notebooks and prediction exports

- [Static comparisons](static-significance-tests/README.md): three tests and static prediction collection.
- [Dynamic and Static–Dynamic comparisons](dynamic-significance-tests/README.md): six tests and dynamic prediction collection.

The `result-reports` directory contains the synthesis and individual reports; generated numeric tables remain in each analysis directory's `statistical_results` folder.

## Inference scope

Image/Multimodal accuracies use 756 view predictions; FEA uses 378 reenactments. Eight primary comparisons use a centered paired reenactment bootstrap, retaining both views together. Static versus Dynamic FEA uses exact McNemar. The nine primary tests are nominal, without a joint correction; the separately reported secondary families use Holm adjustment. Reenactments from the same participant and model-training variability are not modeled by these primary tests.

Sequence-order ablations use their own two-test Holm families and are documented in [Section 5](../../5_dynamic_facial_expression_recognition/README.md).
