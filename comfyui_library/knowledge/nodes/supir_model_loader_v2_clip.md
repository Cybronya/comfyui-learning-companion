# SUPIR_model_loader_v2_clip

## 节点类型

`SUPIR_model_loader_v2_clip`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `model:MODEL`（5 次）
- `clip_l:CLIP`（5 次）
- `clip_g:CLIP`（5 次）
- `vae:VAE`（5 次）
- `supir_model:COMBO`（5 次）
- `fp8_unet:BOOLEAN`（5 次）
- `diffusion_dtype:COMBO`（5 次）
- `high_vram:BOOLEAN`（5 次）

## 输出

- `SUPIR_model:SUPIRMODEL`（5 次）
- `SUPIR_VAE:SUPIRVAE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["SUPIR-v0Q_fp16.safetensors", false, "auto", false]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
