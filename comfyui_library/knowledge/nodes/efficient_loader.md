# Efficient Loader

## 节点类型

`Efficient Loader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `lora_stack:LORA_STACK`（6 次）
- `cnet_stack:CONTROL_NET_STACK`（6 次）
- `empty_latent_width:INT`（1 次）
- `empty_latent_height:INT`（1 次）

## 输出

- `MODEL:MODEL`（6 次）
- `CONDITIONING+:CONDITIONING`（6 次）
- `CONDITIONING-:CONDITIONING`（6 次）
- `LATENT:LATENT`（6 次）
- `VAE:VAE`（6 次）
- `CLIP:CLIP`（6 次）
- `DEPENDENCIES:DEPENDENCIES`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["crystalClearXL_ccxl.safetensors", "Baked VAE", -1, "None", 1, 1, "World architecture", "", "none", "comfy", 1216, 832,`（1 次）
- `["MR 3DQ _SDXL V0.2.safetensors", "Baked VAE", -2, "None", 0.8, 1, "blindbox, 1boy, solo, blonde hair, short hair, hat, `（1 次）
- `["Virtual Utopia_V1.safetensors", "sdxl_vae.safetensors", -1, "None", 1, 1, "1girl, authentic picture,\n\n 8k,highres,HD`（1 次）
- `["authentic utopia 真实乌托邦 XL_V1.safetensors", "sdxl_vae.safetensors", -2, "None", 1, 1, "CLIP_POSITIVE", "", "none", "A11`（1 次）
- `["authentic utopia 真实乌托邦 XL_V1.safetensors", "sdxl_vae.safetensors", -2, "None", 0.8, 1, "C4D, 3D rendering, pandy lying`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
