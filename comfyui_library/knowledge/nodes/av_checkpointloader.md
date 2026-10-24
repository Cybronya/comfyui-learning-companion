# AV_CheckpointLoader

## 节点类型

`AV_CheckpointLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `lora_stack:LORA_STACK`（1 次）
- `cnet_stack:CONTROL_NET_STACK`（1 次）
- `ckpt_name:COMBO`（1 次）
- `vae_name:COMBO`（1 次）
- `clip_skip:INT`（1 次）
- `lora_name:COMBO`（1 次）
- `lora_model_strength:FLOAT`（1 次）
- `lora_clip_strength:FLOAT`（1 次）
- `positive:STRING`（1 次）
- `negative:STRING`（1 次）

## 输出

- `MODEL:MODEL`（1 次）
- `CONDITIONING+:CONDITIONING`（1 次）
- `CONDITIONING-:CONDITIONING`（1 次）
- `LATENT:LATENT`（1 次）
- `VAE:VAE`（1 次）
- `CLIP:CLIP`（1 次）
- `DEPENDENCIES:DEPENDENCIES`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["万象熔炉Anything XL.safetensors", "Baked VAE", -1, "None", 1, 1, "masterpiece, best quality, hakurei reimu, 1girl, red bow`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
