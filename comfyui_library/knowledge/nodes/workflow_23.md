# workflow>23

## 节点类型

`workflow>23`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `模型:MODEL`（1 次）
- `anything:*`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `vae_name:COMBO`（1 次）
- `upscale_method:COMBO`（1 次）
- `megapixels:FLOAT`（1 次）
- `lora_name:COMBO`（1 次）

## 输出

- `VAE:VAE`（1 次）
- `Latent:LATENT`（1 次）
- `CONDITIONING:CONDITIONING`（1 次）
- `条件:CONDITIONING`（1 次）
- `patched_model:MODEL`（1 次）
- `any:*`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default", "qwen_image_vae.safetensors", "nearest-exact", 1, "co`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
