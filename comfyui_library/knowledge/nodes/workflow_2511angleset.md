# workflow>2511angleset

## 节点类型

`workflow>2511angleset`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `conditioning:CONDITIONING`（4 次）
- `FluxKontextMultiReferenceLatentMethod conditioning:CONDITIONING`（4 次）
- `vae_name:COMBO`（4 次）
- `clip_name:COMBO`（4 次）
- `type:COMBO`（4 次）
- `device:COMBO`（4 次）
- `unet_name:COMBO`（4 次）
- `weight_dtype:COMBO`（4 次）
- `lora_name:COMBO`（4 次）

## 输出

- `VAE:VAE`（4 次）
- `CLIP:CLIP`（4 次）
- `IMAGE:IMAGE`（4 次）
- `VAEDecode IMAGE:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen_image_vae.safetensors", "qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default", "qwen_image_edit_2511_b`（1 次）
- `["qwen_image_vae.safetensors", "qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default", "qwen_image_edit_2511_b`（1 次）
- `["qwen_image_vae.safetensors", "qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default", "qwen_image_edit_2511_b`（1 次）
- `["qwen_image_vae.safetensors", "qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default", "qwen_image_edit_2511_b`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
