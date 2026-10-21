# workflow>qwen

## 节点类型

`workflow>qwen`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive:CONDITIONING`（1 次）
- `latent_image:LATENT`（1 次）
- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `vae_name:COMBO`（1 次）
- `shift:FLOAT`（1 次）
- `text:STRING`（1 次）

## 输出

- `CLIP:CLIP`（1 次）
- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen_image_fp8_e4m3fn-v1.0.safetensors", "default", "qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default", `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
