FROM tensorflow/tensorflow:2.15.0.post1-gpu-jupyter

WORKDIR /workspace

COPY requirements.txt /tmp/requirements.txt

# Keep the TensorFlow 2.15.0.post1 / Python 3.11 GPU stack from the
# official TensorFlow image and reproduce the directly specified package
# versions from the original EmoHeVRDB-SFER tf215 environment.
RUN python -m pip install --no-cache-dir \
    --upgrade-strategy only-if-needed \
    -r /tmp/requirements.txt

EXPOSE 8888

CMD ["bash"]
