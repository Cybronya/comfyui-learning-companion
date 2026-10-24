# workflow>核心节点

## 节点类型

`workflow>核心节点`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `sampler_name:COMBO`（2 次）
- `vae_name:COMBO`（2 次）
- `clip_name:COMBO`（2 次）
- `type:COMBO`（2 次）
- `device:COMBO`（2 次）
- `unet_name:COMBO`（2 次）
- `weight_dtype:COMBO`（2 次）
- `upscale_method:COMBO`（2 次）
- `lora_name:COMBO`（2 次）
- `strength_model:FLOAT`（2 次）

## 输出

- `图像:IMAGE`（2 次）
- `降噪输出:LATENT`（1 次）
- `target_image1:IMAGE`（1 次）
- `target_image2:IMAGE`（1 次）
- `target_image3:IMAGE`（1 次）
- `vl_resized_image1:IMAGE`（1 次）
- `vl_resized_image2:IMAGE`（1 次）
- `vl_resized_image3:IMAGE`（1 次）
- `conditioning_with_first_ref:CONDITIONING`（1 次）
- `pad_info:ANY`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["euler", "flux2-vae.safetensors", "mistral_3_small_flux2_fp8.safetensors", "flux2", "default", "flux2_dev_fp8mixed.safe`（1 次）
- `["qwen_image_edit_2511_bf16.safetensors", "fp8_e4m3fn", "qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default"`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
