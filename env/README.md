# Environment and Dataset Setup

[Repository README](../README.md)

The root environment supports dynamic training/inference and the analysis notebooks. [Dockerfile](Dockerfile) uses `nvcr.io/nvidia/tensorflow:25.02-tf2-py3`; [requirements.txt](requirements.txt) includes Keras 3.12.0. Static model inference uses the separate [TensorFlow/Keras 2.15 environment](../4_static_facial_expression_recognition/env/README.md).

## Workspace layout

The host directories are hardcoded in the `volumes` entries of [compose.yml](compose.yml):

```yaml
volumes:
  - /home/thorben/workspace/repos:/workspace/repos
  - /home/thorben/workspace/datasets:/workspace/datasets
```

Edit the left-hand paths directly for another host. The right-hand paths define the container layout used by the notebooks. The repository is expected at `/workspace/repos/emohevrdb-dfer`.

Obtain the published subsets through [EmoHeVRDB access instructions](https://github.com/thorbenortmann/emoji-hero-vr-database#request-access-to-emohevrdb). Place the extracted folders directly under `/workspace/datasets`, retaining their internal structure:

| Folder | Used by | Contents |
| --- | --- | --- |
| `emoji-hero-vr-db-si` | Static Image/Multimodal inference | `test_set/` |
| `emoji-hero-vr-db-sfea-as-csv` | Static FEA/Multimodal inference | `test_set.csv` |
| `emoji-hero-vr-db-di` | Dynamic Image/Multimodal | `training_set/`, `validation_set/`, `test_set/` |
| `emoji-hero-vr-db-dfea-as-csv` | Dynamic FEA/Multimodal and raw-FEA analyses | `training_set.csv`, `validation_set.csv`, `test_set.csv` |

The two static subsets are needed only when regenerating static predictions. Included prediction CSVs support prediction-based analyses without raw datasets or model files.

## Run notebooks

From this directory:

```bash
docker compose up --build
```

Compose configures an NVIDIA GPU and exposes JupyterLab on port 8888. Open the URL printed by the container. GPU/resource settings and volume paths are configured directly in the YAML. Both environments use port 8888; run one at a time with the supplied settings. Stop with `docker compose down`.

Run each notebook with its containing directory as the kernel's working directory. Execute cells in order. Relative input/output paths resolve from that directory; training runs create new timestamped result directories.

Checkpoint downloads are documented in [static models](../4_static_facial_expression_recognition/models/README.md), [dynamic models](../5_dynamic_facial_expression_recognition/models/README.md), [fusion setup](../5_dynamic_facial_expression_recognition/5_3_multimodal/README.md#model-setup), and the sequence-order collector READMEs.
