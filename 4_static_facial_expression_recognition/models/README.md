# Static Model Checkpoints

[Section 4](../README.md)

Save the checkpoints in this directory using these filenames:

| Model | Required local filename | Download |
|---|---|---|
| Image — EfficientNet-B0 | `image_model.keras` | [Google Drive](https://drive.google.com/file/d/1dWeQEf4VkhsVXUWwITMN09Ya-cBVsuNY/view?usp=sharing) |
| FEA — MLP | `fea_model.keras` | [Google Drive](https://drive.google.com/file/d/1Pbd3CRPjY2B_jn9ilHyEGZ10RkNgzV4L/view?usp=sharing) |
| Multimodal — intermediate cross-attention fusion | `multimodal_model.keras` | [Google Drive](https://drive.google.com/file/d/1qqxmZ4NNWb1bqEZ73BL4SSt-I0v-M1R0/view?usp=sharing) |


The [collector](../collect_static_test_predictions.ipynb) loads them with `compile=False`, supplies the custom `CrossAttention` layer, and remaps the legacy output order. Use the [static inference environment](../env/README.md). Model files are external to Git; the shared prediction CSV is already included.
