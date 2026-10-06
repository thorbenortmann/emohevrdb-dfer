# Section 6.3: human annotation agreement and multimodal errors

Test data: 756 view predictions from 378 reenactments and 8 participants; 139 multimodal errors.

- 2/3 agreement: 103/378 reenactments (27.25%).
- Errors on 2/3 cases: 62/139 of all errors (44.60%).
- Error rates: 62/206 = 30.10% for 2/3, and 77/550 = 14.00% for 3/3.
- Raw 3/3 accuracy advantage: 16.10 percentage points.
- Equal weighting of 6 shared classes: 71.01% accuracy for 2/3, 80.89% for 3/3, a 9.88-percentage-point advantage.
- Dissenting-label correspondence: 49/62 erroneous 2/3-agreement view predictions (79.03%).

Annotation source: https://github.com/thorbenortmann/emoji-hero-vr-database/blob/deee4796cbdbfbd39ce70e99c7adb8836feee86e/v_data_annotation/b_results/labels-master-table-analysis_irr.csv

Annotation SHA256: f06ae02ac6f4118e27558fa08303eadcabc9f90b01ae851867c1a1f9cf894d19

Prediction SHA256: ac322c3232bd9a8bcb46f1be049233c2260b3193ebd19197c421ea372e007cde

The complete unchanged annotation CSV is filtered by joining to the shared test predictions. The three raters judged one selected central-view reference image per reenactment; both camera views inherit those annotations. These are descriptive associations, with no inferential tests, confidence intervals, or label corrections. Equal class weighting controls only class composition; it does not establish a causal agreement effect.

Supporting tables: agreement_group_summary.csv, class_recall_by_agreement.csv, equal_class_accuracy_summary.csv, dissenting_label_correspondence.csv, input_provenance.csv.
