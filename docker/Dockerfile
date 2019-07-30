FROM tensorflow:latest

RUN apt update && apt install -y python3-scipy cmake wget libfreetype6-dev

RUN pip3 install keras==2.2.4 \
                 editdistance==0.3.1 \
                 matplotlib==2.0.0 \
                 python-dateutil==2.6.0 \
                 Theano==0.9.0 \
                 nltk==3.2.2 \
                 sk-video==1.1.7
                 
# install dlib 19.16.0
# https://devtalk.nvidia.com/default/topic/1049660/jetson-nano/issues-with-dlib-library/post/5336330/#5336330
RUN wget http://dlib.net/files/dlib-19.16.tar.bz2 && \
    tar jxvf dlib-19.16.tar.bz2 && \
    cd dlib-19.16 && \
    find . -name 'cudnn_dlibapi.cpp' -exec sed -i '/forward_algo\ =\ forward_best_algo/d' {} \; &&\
    mkdir build && \
    cd build && \
    cmake .. && \
    cmake --build . && \
    cd /tmp/dlib-19.16 && \
    python3 setup.py install  

RUN cd /tmp && \
    rm -rf dlib*