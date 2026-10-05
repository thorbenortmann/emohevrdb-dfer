# FEA Analysis Data and Semantic Mapping

[Up one level](../README.md) · [Repository home](../../../README.md)

This directory holds the inputs and saved data-validation metadata used by the parent FEA analysis workflow.

## Available files

- [canonical_dataset_validation.json](canonical_dataset_validation.json): saved validation of split sizes, feature count, sequence length, and reference-observation positions.
- [facs_fea_mapping.json](facs_fea_mapping.json): mapping consumed by the analysis notebooks.
- [Mapping documentation](facs_fea_mapping/README.md): semantic crosswalk, interpretation rules, and source references.

## Generated local inputs

The [canonical dataset generator](../create_canonical_fea_analysis_datasets.ipynb) produces `dfea_train.csv`, `dfea_validation.csv`, `dfea_test.csv`, `sfea_train.csv`, `sfea_validation.csv`, and `sfea_test.csv` from the external source datasets. These six generated CSVs are excluded from the supplied snapshot. They are prerequisites for the raw-coefficient analyses, rather than links to files shipped here.

DFEA uses `(reenactment_id, timestep)` with 30 chronological observations and 63 coefficients. SFEA has one reference observation per reenactment. Expected split counts are 964 Train, 385 Validation, and 378 Test reenactments. Preserve split membership and timestamps when joining to model predictions.

The structured mapping also exists inside `facs_fea_mapping/`; preserve consistency between the two copies if editing it.
