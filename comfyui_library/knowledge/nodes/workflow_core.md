# workflow>core

## 节点类型

`workflow>core`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `latent:LATENT`（1 次）
- `ReferenceLatent latent:LATENT`（1 次）
- `model:MODEL`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `vae_name:COMBO`（1 次）
- `unet_name:COMBO`（1 次）

## 输出

- `VAE:VAE`（1 次）
- `MODEL:MODEL`（1 次）
- `Reroute VAE:VAE`（1 次）
- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `original_size:BOX`（1 次）
- `LATENT:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen_3_8b_fp8mixed.safetensors", "flux2", "default", "flux2-vae.safetensors", "Flux2-Klein-9B-True-v2-fp8mixed.safeten`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
