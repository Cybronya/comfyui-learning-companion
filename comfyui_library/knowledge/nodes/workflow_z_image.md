# workflow>Z-image

## 节点类型

`workflow>Z-image`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `vae_name:COMBO`（1 次）

## 输出

- `MODEL:MODEL`（1 次）
- `CLIP:CLIP`（1 次）
- `VAE:VAE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["zImagePro_v11.safetensors", "default", "qwen_3_4b.safetensors", "stable_diffusion", "default", "ae.safetensors"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
