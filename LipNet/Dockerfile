FROM tensorflow/tensorflow:1.0.1-gpu
WORKDIR /tmp
RUN apt update && apt install -y python-pip wget libfreetype6-dev ffmpeg python-tk cmake

RUN pip install \
    keras==2.0.2 \
    editdistance==0.3.1 \
    h5py==2.6.0 \
    matplotlib==2.0.0 \
    numpy==1.12.1 \
    python-dateutil==2.6.0 \
    scipy==0.19.0 \
    Pillow==4.1.0 \
    Theano==0.9.0 \
    nltk==3.2.2 \
    scikit-video==1.1.11 \
    dlib==19.16.0 \
    jupyterlab


RUN mkdir /app

WORKDIR /app

ENV PYTHONPATH=/app
