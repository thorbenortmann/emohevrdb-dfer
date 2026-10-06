# Dynamic FER Environment

[Repository README](../README.md) · [Section 5](../5_dynamic_facial_expression_recognition/README.md)

This environment runs the dynamic FER notebooks. [Dockerfile](Dockerfile) uses the NVIDIA TensorFlow container; [requirements.txt](requirements.txt) specifies the additional packages, including Keras 3.12.0.

## Workspace and datasets

The hardcoded volume mappings in [compose.yml](compose.yml) make the host's repository and dataset folders available inside the container as `/workspace/repos` and `/workspace/datasets`. Edit these mappings directly if your host folders differ.

The notebooks assume the repository is at `/workspace/repos/emohevrdb-dfer` and these extracted dataset folders are placed directly under `/workspace/datasets`:

| Dataset folder | Used by | Required contents |
| --- | --- | --- |
| `emoji-hero-vr-db-di` | Image and multimodal notebooks | `training_set/`, `validation_set/`, `test_set/` |
| `emoji-hero-vr-db-dfea-as-csv` | FEA and multimodal notebooks | `training_set.csv`, `validation_set.csv`, `test_set.csv` |

Retain the original structure within each dataset folder.

## Running notebooks

From this environment directory, start the container with:

```bash
docker compose up --build
```

Compose configures an NVIDIA GPU and exposes Jupyter Lab on port 8888. Use the URL and token printed in its output; adjust the GPU and resource settings directly in the YAML if needed.

Start each notebook with its containing directory as the kernel's working directory, then run its cells in order. Relative model and output paths are resolved from that directory. Training notebooks create a new timestamped results directory; rerunning a notebook inside a saved-run folder creates a new subdirectory there.

Checkpoint downloads and placement are documented in [Section 5 models](../5_dynamic_facial_expression_recognition/models/README.md), the [fusion model setup](../5_dynamic_facial_expression_recognition/5_3_multimodal/README.md#model-setup), and the two sequence-order collector READMEs.

The included prediction CSVs support subsequent analyses without rerunning training or inference.
