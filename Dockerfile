# Use PyTorch 2.6 GPU base image with Python 3.11 and CUDA 12.1/12.4 on Ubuntu 22.04
FROM pytorch/pytorch:2.6.0-cuda12.1-cudnn8-runtime

ENV DEBIAN_FRONTEND=noninteractive

# metainformation
LABEL org.opencontainers.image.source = "https://github.com/FunAudioLLM/InspireMusic"
LABEL org.opencontainers.image.licenses = "Apache License 2.0"

# Set the working directory
WORKDIR /workspace/InspireMusic
# Copy the current directory contents into the container at /workspace/InspireMusic
COPY .

# inatall library dependencies
RUN apt-get update && apt-get install -y ffmpeg sox libsox-dev git && apt-get clean
RUN pip install --no-cache-dir -r requirements.txt

# install flash attention
RUN pip install flash-attn --no-build-isolation

# download models
RUN mkdir -p /workspace/InspireMusic/pretrained_models
RUN cd /workspace/InspireMusic/pretrained_models
RUN git clone https://modelscope.cn/models/iic/InspireMusic-1.5B-Long.git
RUN git clone https://modelscope.cn/models/iic/InspireMusic.git
RUN git clone https://modelscope.cn/models/iic/InspireMusic-1.5B.git
RUN git clone https://modelscope.cn/models/iic/InspireMusic-Base-24kHz.git
RUN git clone https://modelscope.cn/models/iic/InspireMusic-1.5B-24kHz.git

