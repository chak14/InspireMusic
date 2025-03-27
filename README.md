<p align="center"> <a href="https://github.com/FunAudioLLM/InspireMusic" target="_blank"> <img alt="logo" src="./asset/logo.png" width="100%"></a></p>

<p align="center">
 <a href="https://funaudiollm.github.io/inspiremusic" target="_blank"><img alt="Demo" src="https://img.shields.io/badge/Demo-InspireMusic?labelColor=%20%23FDB062&label=InspireMusic&color=%20%23f79009"></a>
<a href="https://github.com/FunAudioLLM/InspireMusic" target="_blank"><img alt="Code" src="https://img.shields.io/badge/Code-InspireMusic?labelColor=%20%237372EB&label=InspireMusic&color=%20%235462eb"></a>
<a href="https://modelscope.cn/models/iic/InspireMusic-1.5B-Long" target="_blank"><img alt="Model" src="https://img.shields.io/badge/InspireMusic-Model-green"></a>
<a href="https://modelscope.cn/studios/iic/InspireMusic/summary" target="_blank"><img alt="Space" src="https://img.shields.io/badge/Spaces-ModelScope-pink?labelColor=%20%237b8afb&label=Spaces&color=%20%230a5af8"></a>
<a href="https://huggingface.co/spaces/FunAudioLLM/InspireMusic" target="_blank"><img alt="Space" src="https://img.shields.io/badge/HuggingFace-Spaces?labelColor=%20%239b8afb&label=Spaces&color=%20%237a5af8"></a>
<a href="http://arxiv.org/abs/2503.00084" target="_blank"><img alt="Paper" src="https://img.shields.io/badge/arXiv-Paper-green"></a>
</p>

InspireMusic is a fundamental AIGC toolkit and models designed for music, song, and audio generation. 

![GitHub Repo stars](https://img.shields.io/github/stars/FunAudioLLM/InspireMusic) Please support our community 💖 by starring it 感谢大家加⭐支持🙏 

[**Highlights**](#highlights)
| [**News**](https://github.com/FunAudioLLM/InspireMusic#whats-new) 
| [**Introduction**](#introduction)
| [**Installation**](#installation)
| [**Quick Start**](#quick-start)
| [**Tutorial**](https://github.com/FunAudioLLM/InspireMusic#tutorial)
| [**Models**](#model-zoo)
| [**Contact**](#contact)

---
<a name="highlights"></a>
## Highlights
**InspireMusic** focuses on music generation, song generation, and audio generation.
- A unified framework designed for music, song, and audio generation. Controllable with text prompts, music genres, music structures, etc.
- Currently, support music generation tasks with high audio quality. 
- Support long-form music generation.
- Convenient fine-tuning and inference. Support mixed precision training (e.g., BF16, FP16, FP32). Provide convenient fine-tuning and inference scripts, allowing users to easily fine-tune and infer models.

<a name="whats-new"></a>
## What's New 
- 2025/03: InspireMusic [Technical Report](http://arxiv.org/abs/2503.00084) is released on arXiv.
- 2025/02: Online demos can be found on [ModelScope Space](https://modelscope.cn/studios/iic/InspireMusic/summary) and [HuggingFace Space](https://huggingface.co/spaces/FunAudioLLM/InspireMusic).
- 2025/01: Open-source [InspireMusic-Base](https://modelscope.cn/models/iic/InspireMusic/summary), [InspireMusic-Base-24kHz](https://modelscope.cn/models/iic/InspireMusic-Base-24kHz/summary), [InspireMusic-1.5B](https://modelscope.cn/models/iic/InspireMusic-1.5B/summary), [InspireMusic-1.5B-24kHz](https://modelscope.cn/models/iic/InspireMusic-1.5B-24kHz/summary), [InspireMusic-1.5B-Long](https://modelscope.cn/models/iic/InspireMusic-1.5B-Long/summary) models for music generation. Models are available on both ModelScope and HuggingFace. 
- 2024/12: Support to generate 48kHz music with super resolution flow matching model.
- 2024/11: Demos preview in [**InspireMusic Demos**](https://funaudiollm.github.io/inspiremusic). We're excited to share this with you and will bring more features, tasks and models soon. Your support and feedback mean a lot to us!
- 2024/11: We are glad to open-source the **InspireMusic** [code repository](https://github.com/FunAudioLLM/InspireMusic) and [demos](https://funaudiollm.github.io/inspiremusic). **InspireMusic** is a unified framework designed for music, song, and audio generation, featuring capabilities such as text-to-music generation, music continuation and so on. InspireMusic shows comparative performance on music generation with currently top-tier open-sourced models.

<a name="introduction"></a>
## Introduction
> [!Note]
> This repo contains the algorithm infrastructure and some simple examples. Currently only support English text prompts.

> [!Tip]
> To preview the performance, please refer to [InspireMusic Demo Page](https://funaudiollm.github.io/inspiremusic).

InspireMusic is a unified music, song, and audio generation framework through the audio tokenization integrated with autoregressive transformer and flow-matching based model. The original motive of this toolkit is to empower the common users to innovate soundscapes and enhance euphony in research through music, song, and audio crafting. The toolkit provides both training and inference codes for AI-based generative models that create high-quality music. Featuring a unified framework, InspireMusic incorporates audio tokenizers with autoregressive transformer and super-resolution flow-matching modeling, allowing for the controllable generation of music, song, and audio with both text and audio prompts. The toolkit currently supports music generation, will support song generation, audio generation in the future.

## InspireMusic
<p align="center"><table><tr><td style="text-align:center;"><img alt="Light" src="asset/InspireMusic.png" width="100%" /></tr><tr><td style="text-align:center;">
Figure 1: An overview of the InspireMusic framework. We introduce InspireMusic, a unified framework for music, song, audio generation capable of producing high-quality long-form audio. InspireMusic consists of the following three key components. <b>Audio Tokenizers</b> convert the raw audio waveform into discrete audio tokens that can be efficiently processed and trained by the autoregressive transformer model. Audio waveform of lower sampling rate has converted to discrete tokens via a high bitrate compression audio tokenizer<a href="https://openreview.net/forum?id=yBlVlS2Fd9" target="_blank"><sup>[1]</sup></a>. <b>Autoregressive Transformer</b> model is based on Qwen2.5<a href="https://arxiv.org/abs/2412.15115" target="_blank"><sup>[2]</sup></a> as the backbone model and is trained using a next-token prediction approach on both text and audio tokens, enabling it to generate coherent and contextually relevant token sequences. The audio and text tokens are the inputs of an autoregressive model with the next token prediction to generate tokens. <b>Super-Resolution Flow-Matching Model</b> based on flow modeling method, maps the generated tokens to latent features with high-resolution fine-grained acoustic details<a href="https://arxiv.org/abs/2305.02765" target="_blank"><sup>[3]</sup></a> obtained from a higher sampling rate of audio to ensure the acoustic information flow connected with high fidelity through models. A vocoder then generates the final audio waveform from these enhanced latent features. InspireMusic supports a range of tasks including text-to-music, music continuation, music reconstruction, and music super-resolution.
</td></tr></table></p>

<a name="installation"></a>
## Installation
### Clone
- Clone the repo
``` sh
git clone --recursive https://github.com/FunAudioLLM/InspireMusic.git
# If you failed to clone submodule due to network failures, please run the following command until success
cd InspireMusic
git submodule update --recursive
# or you can download the third_party repo Matcha-TTS manually
cd third_party && git clone https://github.com/shivammehta25/Matcha-TTS.git
```

### Install from Source
InspireMusic requires Python>=3.8, PyTorch>=2.0.1, flash attention==2.6.2/2.6.3, CUDA>=11.2. You can install the dependencies with the following commands:

- Install Conda: please see https://docs.conda.io/en/latest/miniconda.html
- Create Conda env:
``` shell
conda create -n inspiremusic python=3.8
conda activate inspiremusic
cd InspireMusic
# pynini is required by WeTextProcessing, use conda to install it as it can be executed on all platforms.
conda install -y -c conda-forge pynini==2.1.5
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
# install flash attention to speedup training
pip install flash-attn --no-build-isolation
```

- Install within the package:
```shell
cd InspireMusic
# You can run to install the packages
python setup.py install
pip install flash-attn --no-build-isolation
```
We also recommend having `sox` or `ffmpeg` installed, either through your system or Anaconda:
```shell
# # Install sox
# ubuntu
sudo apt-get install sox libsox-dev
# centos
sudo yum install sox sox-devel

# Install ffmpeg
# ubuntu
sudo apt-get install ffmpeg
# centos
sudo yum install ffmpeg
```

### Use Docker
Run the following command to build a docker image from Dockerfile provided.
```shell
docker build -t inspiremusic .
```
Run the following command to start the docker container in interactive mode.
```shell
docker run -ti --gpus all -v .:/workspace/InspireMusic inspiremusic
```

### Use Docker Compose
Run the following command to build a docker compose environment and docker image from the docker-compose.yml file.
```shell
docker compose up -d --build
```
Run the following command to attach to the docker container in interactive mode.
```shell
docker exec -ti inspire-music bash
```

<a name="quick-start"></a>
### Quick Start
Here is a quick example inference script for music generation. 
``` shell
cd InspireMusic
mkdir -p pretrained_models

# Download models
# ModelScope
git clone https://www.modelscope.cn/iic/InspireMusic-1.5B-Long.git pretrained_models/InspireMusic-1.5B-Long
# HuggingFace
git clone https://huggingface.co/FunAudioLLM/InspireMusic-1.5B-Long.git pretrained_models/InspireMusic-1.5B-Long

cd examples/music_generation
# run a quick inference example
sh infer_1.5b_long.sh
```

Here is a quick start running script to run music generation task including data preparation pipeline, model training, inference. 
``` shell
cd InspireMusic/examples/music_generation/
sh run.sh
```

### One-line Inference
#### Text-to-music Task
One-line Shell script for text-to-music task.
``` shell
cd examples/music_generation
# with flow matching, use one-line command to get a quick try
python -m inspiremusic.cli.inference

# custom the config like the following one-line command
python -m inspiremusic.cli.inference --task text-to-music -m "InspireMusic-1.5B-Long" -g 0 -t "Experience soothing and sensual instrumental jazz with a touch of Bossa Nova, perfect for a relaxing restaurant or spa ambiance." -c intro -s 0.0 -e 30.0 -r "exp/inspiremusic" -o output -f wav 

# without flow matching, use one-line command to get a quick try
python -m inspiremusic.cli.inference --task text-to-music -g 0 -t "Experience soothing and sensual instrumental jazz with a touch of Bossa Nova, perfect for a relaxing restaurant or spa ambiance." --fast True
```

Alternatively, you can run the inference with just a few lines of Python code.
```python
from inspiremusic.cli.inference import InspireMusic
from inspiremusic.cli.inference import env_variables
if __name__ == "__main__":
  env_variables()
  model = InspireMusic(model_name = "InspireMusic-Base")
  model.inference("text-to-music", "Experience soothing and sensual instrumental jazz with a touch of Bossa Nova, perfect for a relaxing restaurant or spa ambiance.")
```

#### Music Continuation Task
One-line Shell script for music continuation task.
```shell
cd examples/music_generation
# with flow matching
python -m inspiremusic.cli.inference --task continuation -g 0 -a audio_prompt.wav
# without flow matching
python -m inspiremusic.cli.inference --task continuation -g 0 -a audio_prompt.wav --fast True
```

Alternatively, you can run the inference with just a few lines of Python code.
```python
from inspiremusic.cli.inference import InspireMusic
from inspiremusic.cli.inference import env_variables
if __name__ == "__main__":
  env_variables()
  model = InspireMusic(model_name = "InspireMusic-Base")
  # just use audio prompt
  model.inference("continuation", None, "audio_prompt.wav")
  # use both text prompt and audio prompt
  model.inference("continuation", "Continue to generate jazz music.", "audio_prompt.wav")
```
<a name="model-zoo"></a>
## Models
### Download Models
You may download our pretrained InspireMusic models for music generation.
```shell
# use git to download models，please make sure git lfs is installed.
mkdir -p pretrained_models
git clone https://www.modelscope.cn/iic/InspireMusic.git pretrained_models/InspireMusic
```

### Available Models
Currently, we open source the music generation models support 24KHz mono and 48KHz stereo audio. 
The table below presents the links to the ModelScope and Huggingface model hub. More models will be available soon.

| Model name                           | Model Links                                                                                                                                                                                                                                                                                                                                   | Remarks                                                                                                  |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| InspireMusic-Base-24kHz              | [![model](https://img.shields.io/badge/ModelScope-Model-green.svg)](https://modelscope.cn/models/iic/InspireMusic-Base-24kHz/summary) [![model](https://img.shields.io/badge/HuggingFace-Model-green.svg)](https://huggingface.co/FunAudioLLM/InspireMusic-Base-24kHz)                                                                        | Pre-trained Music Generation Model, 24kHz mono, 30s                                                      |
| InspireMusic-Base                    | [![model](https://img.shields.io/badge/ModelScope-Model-green.svg)](https://modelscope.cn/models/iic/InspireMusic/summary) [![model](https://img.shields.io/badge/HuggingFace-Model-green.svg)](https://huggingface.co/FunAudioLLM/InspireMusic-Base)                                                                                         | Pre-trained Music Generation Model, 48kHz, 30s                                                           |
| InspireMusic-1.5B-24kHz              | [![model](https://img.shields.io/badge/ModelScope-Model-green.svg)](https://modelscope.cn/models/iic/InspireMusic-1.5B-24kHz/summary) [![model](https://img.shields.io/badge/HuggingFace-Model-green.svg)](https://huggingface.co/FunAudioLLM/InspireMusic-1.5B-24kHz)                                                                        | Pre-trained Music Generation 1.5B Model, 24kHz mono, 30s                                                 |
| InspireMusic-1.5B                    | [![model](https://img.shields.io/badge/ModelScope-Model-green.svg)](https://modelscope.cn/models/iic/InspireMusic-1.5B/summary) [![model](https://img.shields.io/badge/HuggingFace-Model-green.svg)](https://huggingface.co/FunAudioLLM/InspireMusic-1.5B)                                                                                    | Pre-trained Music Generation 1.5B Model, 48kHz, 30s                                                      |
| InspireMusic-1.5B-Long               | [![model](https://img.shields.io/badge/ModelScope-Model-green.svg)](https://modelscope.cn/models/iic/InspireMusic-1.5B-Long/summary) [![model](https://img.shields.io/badge/HuggingFace-Model-green.svg)](https://huggingface.co/FunAudioLLM/InspireMusic-1.5B-Long)                                                                          | Pre-trained Music Generation 1.5B Model, 48kHz, support long-form music generation up to several minutes |
| InspireSong-1.5B                     | [![model](https://img.shields.io/badge/ModelScope-Model-lightgrey.svg)]() [![model](https://img.shields.io/badge/HuggingFace-Model-lightgrey.svg)]()                                                                                                                                                                                          | Pre-trained Song Generation 1.5B Model, 48kHz stereo                                                     |
| InspireAudio-1.5B                    | [![model](https://img.shields.io/badge/ModelScope-Model-lightgrey.svg)]() [![model](https://img.shields.io/badge/HuggingFace-Model-lightgrey.svg)]()                                                                                                                                                                                          | Pre-trained Audio Generation 1.5B Model, 48kHz stereo                                                    |
| Wavtokenizer[<sup>[1]</sup>](https://openreview.net/forum?id=yBlVlS2Fd9) (75Hz) | [![model](https://img.shields.io/badge/ModelScope-Model-green.svg)](https://modelscope.cn/models/iic/InspireMusic-1.5B-Long/file/view/master?fileName=wavtokenizer%252Fmodel.pt) [![model](https://img.shields.io/badge/HuggingFace-Model-green.svg)](https://huggingface.co/FunAudioLLM/InspireMusic-1.5B-Long/tree/main/wavtokenizer)       | An extreme low bitrate audio tokenizer for music with one codebook at 24kHz audio.                       |
| Music_tokenizer (75Hz)               | [![model](https://img.shields.io/badge/ModelScope-Model-green.svg)](https://modelscope.cn/models/iic/InspireMusic-1.5B-24kHz/file/view/master?fileName=music_tokenizer%252Fmodel.pt) [![model](https://img.shields.io/badge/HuggingFace-Model-green.svg)](https://huggingface.co/FunAudioLLM/InspireMusic-1.5B-24kHz/tree/main/music_tokenizer) | A music tokenizer based on HifiCodec<sup>[3]</sup> at 24kHz audio.                                       |
| Music_tokenizer (150Hz)              | [![model](https://img.shields.io/badge/ModelScope-Model-green.svg)](https://modelscope.cn/models/iic/InspireMusic-1.5B-Long/file/view/master?fileName=music_tokenizer%252Fmodel.pt) [![model](https://img.shields.io/badge/HuggingFace-Model-green.svg)](https://huggingface.co/FunAudioLLM/InspireMusic-1.5B-Long/tree/main/music_tokenizer) | A music tokenizer based on HifiCodec<sup>[3]</sup> at 48kHz audio.                                       |

Our models have been trained within a limited budget, and there is still significant potential for performance improvement. We are actively working on enhancing the model's performance.

<a name="tutorial"></a>
## Basic Usage
At the moment, InspireMusic contains the training and inference codes for [music generation](https://github.com/FunAudioLLM/InspireMusic/tree/main/examples/music_generation). More tasks such as song generation, audio generation will be supported in the future.

### Training
Here is an example to train LLM model, support BF16/FP16 training. 
```shell
torchrun --nnodes=1 --nproc_per_node=8 \
    --rdzv_id=1024 --rdzv_backend="c10d" --rdzv_endpoint="localhost:0" \
    inspiremusic/bin/train.py \
    --train_engine "torch_ddp" \
    --config conf/inspiremusic.yaml \
    --train_data data/train.data.list \
    --cv_data data/dev.data.list \
    --model llm \
    --model_dir `pwd`/exp/music_generation/llm/ \
    --tensorboard_dir `pwd`/tensorboard/music_generation/llm/ \
    --ddp.dist_backend "nccl" \
    --num_workers 8 \
    --prefetch 100 \
    --pin_memory \
    --deepspeed_config ./conf/ds_stage2.json \
    --deepspeed.save_states model+optimizer \
    --fp16
```

Here is an example code to train flow matching model, does not support FP16 training.
```shell
torchrun --nnodes=1 --nproc_per_node=8 \
    --rdzv_id=1024 --rdzv_backend="c10d" --rdzv_endpoint="localhost:0" \
    inspiremusic/bin/train.py \
    --train_engine "torch_ddp" \
    --config conf/inspiremusic.yaml \
    --train_data data/train.data.list \
    --cv_data data/dev.data.list \
    --model flow \
    --model_dir `pwd`/exp/music_generation/flow/ \
    --tensorboard_dir `pwd`/tensorboard/music_generation/flow/ \
    --ddp.dist_backend "nccl" \
    --num_workers 8 \
    --prefetch 100 \
    --pin_memory \
    --deepspeed_config ./conf/ds_stage2.json \
    --deepspeed.save_states model+optimizer
```

### Inference

Here is an example script to quickly do model inference.
```shell
cd InspireMusic/examples/music_generation/
sh infer.sh
```
Here is an example code to run inference with normal mode, i.e., with flow matching model for text-to-music and music continuation tasks.
```shell
pretrained_model_dir = "pretrained_models/InspireMusic/"
for task in 'text-to-music' 'continuation'; do
  python inspiremusic/bin/inference.py --task $task \
      --gpu 0 \
      --config conf/inspiremusic.yaml \
      --prompt_data data/test/parquet/data.list \
      --flow_model $pretrained_model_dir/flow.pt \
      --llm_model $pretrained_model_dir/llm.pt \
      --music_tokenizer $pretrained_model_dir/music_tokenizer \
      --wavtokenizer $pretrained_model_dir/wavtokenizer \
      --result_dir `pwd`/exp/inspiremusic/${task}_test \
      --chorus verse \
      --min_generate_audio_seconds 8 \
      --max_generate_audio_seconds 30 
done
```
Here is an example code to run inference with fast mode, i.e., without flow matching model for text-to-music and music continuation tasks.
```shell
pretrained_model_dir = "pretrained_models/InspireMusic/"
for task in 'text-to-music' 'continuation'; do
  python inspiremusic/bin/inference.py --task $task \
      --gpu 0 \
      --config conf/inspiremusic.yaml \
      --prompt_data data/test/parquet/data.list \
      --flow_model $pretrained_model_dir/flow.pt \
      --llm_model $pretrained_model_dir/llm.pt \
      --music_tokenizer $pretrained_model_dir/music_tokenizer \
      --wavtokenizer $pretrained_model_dir/wavtokenizer \
      --result_dir `pwd`/exp/inspiremusic/${task}_test \
      --chorus verse \
      --fast \
      --min_generate_audio_seconds 8 \
      --max_generate_audio_seconds 30 
done
```

### Hardware & Execution Time
Previous test on H800 GPU, InspireMusic-1.5B-Long could generate 30 seconds audio with real-time factor (RTF) around 1.6~1.8. For normal mode, we recommend using hardware with at least 24GB of GPU memory for better experience. For fast mode, 12GB GPU memory is enough. If you want to generate longer audio, you may increase the `--max_generate_audio_seconds` inference parameter with larger GPU memory. Support inference on Linux/Unix, macOS, Windows systems. 

## Roadmap
- [x] 2024/12
  - [x] 75Hz InspireMusic-Base model for music generation
    
- [x] 2025/01
    - [x] Support to generate 48kHz
    - [x] 75Hz InspireMusic-1.5B model for music generation
    - [x] 75Hz InspireMusic-1.5B-Long model for long-form music generation

- [x] 2025/02
    - [x] Technical report v1
    - [x] Provide Dockerfile

- [ ] 2025
    - [ ] Support audio generation task
    - [ ] InspireAudio model for audio generation
    - [ ] Support song generation task
    - [ ] InspireSong model for song generation

- [ ] TBD
    - [ ] Diverse sampling strategies
    - [ ] 25Hz InspireMusic model
    - [ ] Runtime SDK
    - [ ] Support streaming inference mode 
    - [ ] Support more diverse instruction mode, multi-lingual instructions
    - [ ] InspireSong trained with more multi-lingual data
    - [ ] More...

## Citation
```bibtex
@misc{InspireMusic2025,
      title={InspireMusic: Integrating Super Resolution and Large Language Model for High-Fidelity Long-Form Music Generation}, 
      author={Chong Zhang and Yukun Ma and Qian Chen and Wen Wang and Shengkui Zhao and Zexu Pan and Hao Wang and Chongjia Ni and Trung Hieu Nguyen and Kun Zhou and Yidi Jiang and Chaohong Tan and Zhifu Gao and Zhihao Du and Bin Ma},
      year={2025},
      eprint={2503.00084},
      archivePrefix={arXiv},
      primaryClass={cs.SD},
      url={https://arxiv.org/abs/2503.00084}, 
}
```
---
### Friend Links
Checkout some awesome open-source projects from Tongyi Lab, Alibaba Group.

<p align="center">
<a href="https://github.com/modelscope/ClearerVoice-Studio" target="_blank">
        <img alt="Demo" src="https://img.shields.io/badge/Repo | Space-ClearVoice?labelColor=&label=ClearVoice&color=green"></a>
<a href="https://github.com/FunAudioLLM/CosyVoice" target="_blank">
        <img alt="Demo" src="https://img.shields.io/badge/Repo | Space-CosyVoice?labelColor=&label=CosyVoice&color=green"></a>
<a href="https://github.com/FunAudioLLM/SenseVoice" target="_blank">
        <img alt="Demo" src="https://img.shields.io/badge/Repo | Space-SenseVoice?labelColor=&label=SenseVoice&color=green"></a>
</p>

<a name="contact"></a>
## Community & Discussion
* Welcome to join our DingTalk and WeChat groups to share and discuss algorithms, technology, and user experience feedback. You may scan the following QR codes to join our official chat groups accordingly.

<p align="center"><table><tr>
<td style="text-align:center;"><a href="./asset/QR.jpg"><img alt="FunAudioLLM in DingTalk" src="https://img.shields.io/badge/FunAudioLLM-DingTalk-green"></a></td>
<td style="text-align:center;"><a href="./asset/QR.jpg"><img alt="InspireMusic in WeChat" src="https://img.shields.io/badge/InspireMusic-WeChat-green"></a></td>
</tr><tr><td style="text-align:center;"><img alt="Light" src="./asset/dingding.png" width="100%" />
<td style="text-align:center;"><img alt="Light" src="./asset/QR.jpg" width="80%" /></td>
</tr></table></p>

* [Github Discussion](https://github.com/FunAudioLLM/InspireMusic/discussions). For sharing feedback and asking questions.
* [GitHub Issues](https://github.com/FunAudioLLM/InspireMusic/issues). For sharing issues and suggestions using InspireMusic and feature proposals.

## Acknowledgement
1. We borrowed a lot of code from [CosyVoice<sup>[4]</sup>](https://github.com/FunAudioLLM/CosyVoice).
3. We borrowed a lot of code from [WavTokenizer<sup>[1]</sup>](https://github.com/jishengpeng/WavTokenizer).
4. We borrowed a lot of code from [AcademiCodec<sup>[3]</sup>](https://github.com/yangdongchao/AcademiCodec).
5. We borrowed a lot of code from [FunASR](https://github.com/modelscope/FunASR).
6. We borrowed a lot of code from [FunCodec](https://github.com/modelscope/FunCodec).
7. We borrowed a lot of code from [Matcha-TTS](https://github.com/shivammehta25/Matcha-TTS).
9. We borrowed a lot of code from [WeNet](https://github.com/wenet-e2e/wenet).

## References
[1] Shengpeng Ji, Ziyue Jiang, Wen Wang, Yifu Chen, Minghui Fang, Jialong Zuo, Qian Yang, Xize Cheng, Zehan Wang, Ruiqi Li, Ziang Zhang, Xiaoda Yang, Rongjie Huang, Yidi Jiang, Qian Chen, Siqi Zheng, Wen Wang, Zhou Zhao, WavTokenizer: an Efficient Acoustic Discrete Codec Tokenizer for Audio Language Modeling, The Thirteenth International Conference on Learning Representations, 2025.

[2] Qwen: An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tianyi Tang, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, Zihan Qiu, Qwen2.5 Technical Report, arXiv preprint arXiv:2412.15115, 2025.

[3] Yang, Dongchao, Songxiang Liu, Rongjie Huang, Jinchuan Tian, Chao Weng, and Yuexian Zou, Hifi-codec: Group-residual vector quantization for high fidelity audio codec, arXiv preprint arXiv:2305.02765, 2023.

[4] Du, Zhihao, Qian Chen, Shiliang Zhang, Kai Hu, Heng Lu, Yexin Yang, Hangrui Hu et al. Cosyvoice: A scalable multilingual zero-shot text-to-speech synthesizer based on supervised semantic tokens. arXiv preprint arXiv:2407.05407, 2024. 

## Disclaimer
The content provided above is for research purposes only and is intended to demonstrate technical capabilities. Some examples are sourced from the internet. If any content infringes on your rights, please contact us to request its removal.
