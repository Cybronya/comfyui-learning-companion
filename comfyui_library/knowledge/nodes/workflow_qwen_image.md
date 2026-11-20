# workflow>qwen image

## 节点类型

`workflow>qwen image`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `TextEncodeQwenImageEditEnhanced image:IMAGE`（3 次）
- `clip_name:COMBO`（3 次）
- `type:COMBO`（3 次）
- `device:COMBO`（3 次）
- `vae_name:COMBO`（3 次）
- `unet_name:COMBO`（3 次）
- `weight_dtype:COMBO`（3 次）
- `lora_name:COMBO`（3 次）
- `strength_model:FLOAT`（3 次）

## 输出

- `图像:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default", "qwen_image_vae.safetensors", "qwen_image_edit_fp8_e4`（1 次）
- `["qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default", "qwen_image_vae.safetensors", "qwen_image_edit_fp8_e4`（1 次）
- `["qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default", "qwen_image_vae.safetensors", "qwen_image_edit_fp8_e4`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
