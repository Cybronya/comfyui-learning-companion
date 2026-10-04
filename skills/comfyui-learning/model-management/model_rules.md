# Model Rules


# 1. Model Discovery


扫描：


ComfyUI/models/


目录：


- checkpoints
- diffusion_models
- vae
- loras
- controlnet
- text_encoders
- embeddings



---


# 2. Model Classification


根据：

- 文件路径
- 文件名
- 文件扩展

判断类型。


---


# Checkpoint Rules


关键词：


- sd
- stable
- checkpoint
- ckpt
- safetensors


类别：


checkpoint



---


# Diffusion Model Rules


关键词：


- wan
- hunyuan
- ltx
- flux
- video


类别：


diffusion_model



---


# VAE Rules


关键词：


vae


类别：


vae



---


# LoRA Rules


关键词：


- lora
- adapter


类别：


lora



---


# 3. Metadata Extraction


记录：


- filename
- path
- size
- format
- hash
- type



---


# 4. Compatibility


建立：


Model

↓

Compatible Nodes


例如：


Wan Model

compatible:

- WanVideoLoader
- WanSampler



---


# 5. VRAM Estimation


根据：


- file_size
- dtype
- architecture


估算：


memory_requirement


仅作为参考。
