FROM nvcr.io/nvidia/tensorflow:25.02-tf2-py3

WORKDIR /workspace

COPY requirements.txt /workspace/

RUN pip install --upgrade-strategy only-if-needed -r requirements.txt

EXPOSE 8888

CMD [ "bash" ]
