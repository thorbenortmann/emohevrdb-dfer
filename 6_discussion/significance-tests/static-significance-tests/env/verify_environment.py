import platform
import sys

import matplotlib
import numpy as np
import sklearn
import tensorflow as tf

try:
    import jupyterlab
    jupyterlab_version = jupyterlab.__version__
except Exception as exc:
    jupyterlab_version = f"unavailable ({exc})"

try:
    import seaborn as sns
    seaborn_version = sns.__version__
except Exception as exc:
    seaborn_version = f"unavailable ({exc})"

print("Python:", sys.version.replace("\n", " "))
print("Platform:", platform.platform())
print("TensorFlow:", tf.__version__)
print("NumPy:", np.__version__)
print("Matplotlib:", matplotlib.__version__)
print("scikit-learn:", sklearn.__version__)
print("seaborn:", seaborn_version)
print("JupyterLab:", jupyterlab_version)
print("Built with CUDA:", tf.test.is_built_with_cuda())
print("Visible GPUs:", tf.config.list_physical_devices("GPU"))

expected = {
    "tensorflow": "2.15.0",
    "numpy": "1.26.4",
    "matplotlib": "3.7.5",
    "scikit-learn": "1.3.2",
    "seaborn": "0.13.2",
    "jupyterlab": "4.0.12",
}
actual = {
    "tensorflow": tf.__version__,
    "numpy": np.__version__,
    "matplotlib": matplotlib.__version__,
    "scikit-learn": sklearn.__version__,
    "seaborn": seaborn_version,
    "jupyterlab": jupyterlab_version,
}

mismatches = {
    name: (expected[name], actual[name])
    for name in expected
    if expected[name] != actual[name]
}

if mismatches:
    print("\nVersion mismatches:")
    for name, (want, got) in mismatches.items():
        print(f"  {name}: expected {want}, got {got}")
    raise SystemExit(1)

if not tf.config.list_physical_devices("GPU"):
    raise SystemExit("\nERROR: TensorFlow does not see a GPU.")

print("\nEnvironment check passed.")
