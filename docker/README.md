## Container setup for TX2

### 1. Build tensorflow container (if you don't already have it)
Skip this if you already have the tensorflow:latest container.

The following instructions were taken from [week05 hw](https://github.com/MIDS-scaling-up/v2/blob/442b45e6e453384a22c28ddbd2471c838ea7de3e/week05/hw/README.md). 

First, you will need to build a Cuda Tensorflow container on your TX2.

First, build the docker container for [Nvidia TensorRT](https://developer.nvidia.com/tensorrt) using the corresponding Dockerfile [here](https://github.com/MIDS-scaling-up/v2/tree/master/backup/tensorrt)

```
# cd to the correct directory after git cloning the class repo
docker build -t tensorrt -f Dockerfile.tx2-4.2_b158 .
```

Now build the docker container for tensorflow using the python3 Dockerfile [here](https://github.com/MIDS-scaling-up/v2/tree/master/backup/tensorflow). Note that at the moment, Nvidia provides no support for Tensorflow with python2 on the Jetson boards.

```
# cd to the correct directory after git cloning the class repo
docker build -t tensorflow -f Dockerfile.dev-tx2-4.2_b158-py3 .
```



### 2. Build the container for LipNet

```
docker build -t lipnet .
```

