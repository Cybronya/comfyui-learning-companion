# Eff. Loader SDXL

## 节点类型

`Eff. Loader SDXL`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `lora_stack:LORA_STACK`（1 次）
- `cnet_stack:CONTROL_NET_STACK`（1 次）
- `base_ckpt_name:COMBO`（1 次）
- `base_clip_skip:INT`（1 次）
- `refiner_ckpt_name:COMBO`（1 次）
- `refiner_clip_skip:INT`（1 次）
- `positive_ascore:FLOAT`（1 次）
- `negative_ascore:FLOAT`（1 次）
- `vae_name:COMBO`（1 次）
- `positive:STRING`（1 次）

## 输出

- `SDXL_TUPLE:SDXL_TUPLE`（1 次）
- `LATENT:LATENT`（1 次）
- `VAE:VAE`（1 次）
- `DEPENDENCIES:DEPENDENCIES`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["SDXL_梦碎_ 真实感大模型 _ NeverDream_FUSION-V1.safetensors", -2, "SDXL_梦碎_ 真实感大模型 _ NeverDream_FUSION-V1.safetensors", -2, 6, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
