# Static Inference Environment

[Section 4](../README.md) · [Shared workspace and datasets](../../env/README.md#workspace-layout)

The frozen static models use TensorFlow/Keras 2.15. [Dockerfile](Dockerfile) starts from `tensorflow/tensorflow:2.15.0.post1-gpu-jupyter`; additional package versions are in [requirements.txt](requirements.txt).

The hardcoded host volume paths in [compose.yml](compose.yml) mount the same repository/dataset layout as the root environment. Edit those paths directly for another host. Dataset folders and required contents are documented once in the [shared setup](../../env/README.md#workspace-layout).

From this directory, with Docker Compose and NVIDIA GPU support:

```bash
docker compose up --build
```

Open the printed JupyterLab URL. Run [collect_static_test_predictions.ipynb](../collect_static_test_predictions.ipynb) from the Section 4 directory after following the [model instructions](../models/README.md). It exports `static_test_predictions.csv` there. Stop the container with `docker compose down`.

This environment is required for static inference, not for analyses using the included prediction CSV.
