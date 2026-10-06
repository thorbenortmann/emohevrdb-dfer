# 5. Dynamic Facial Expression Recognition

[Repository README](../README.md)

Training, evaluation, sequence-order controls, and fusion experiments for Section 5 of the paper.

Environment, workspace layout, datasets, and notebook execution are documented in [env/README.md](../env/README.md).

## Experiments

| Paper section | Directory | Main notebook |
| --- | --- | --- |
| 5.1 Image sequences | [5_1_image](5_1_image/README.md) | [efficientnetv2_lstm.ipynb](5_1_image/efficientnetv2_lstm.ipynb) |
| 5.2 FEA sequences | [5_2_fea](5_2_fea/README.md) | [lstm.ipynb](5_2_fea/lstm.ipynb) |
| 5.3 Multimodal fusion | [5_3_multimodal](5_3_multimodal/README.md) | Complementarity, late fusion, and intermediate fusion |

## Shared test predictions

[dynamic_test_predictions.csv](dynamic_test_predictions.csv) contains predictions from the selected ordered Image, ordered FEA, and intermediate-fusion Multimodal models. It has one row per image view (756 rows from 378 reenactments); each FEA prediction is repeated for the two corresponding views.

To regenerate it, place the three checkpoints in [models/](models/README.md), then run [collect_dynamic_test_predictions.ipynb](collect_dynamic_test_predictions.ipynb). Saved-prediction analyses can use the included CSV without datasets or model inference. Sequence-order comparisons use their own prediction CSVs in Sections 5.1.3 and 5.2.3.

## Paper and supplement

Tables 4–6 report the selected dynamic baselines. The complementarity notebook produces Figure 3; the [intermediate-fusion architecture](5_3_multimodal/5_3_3_intermediate/dfer-intermediate-fusion-compact.pdf) is Figure 4. Experimental settings for Section 5 are described in supplemental Tables S4–S11. The shared [confusion-matrix notebook](../supplemental_material/confusion_matrices.ipynb) produces the dynamic panels in supplemental Figure S3. Further analyses of the shared predictions are in [Section 6](../6_discussion/README.md).
