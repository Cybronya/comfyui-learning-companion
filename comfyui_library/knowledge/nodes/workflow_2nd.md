# workflow>2ND

## 节点类型

`workflow>2ND`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `ImageScaleToTotalPixels image:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `TextEncodeQwenImageEditPlus image3:IMAGE`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `vae_name:COMBO`（1 次）
- `model_name:COMBO`（1 次）
- `cpu_offload:COMBO`（1 次）

## 输出

- `width:INT`（1 次）
- `height:INT`（1 次）
- `upscale_factor:FLOAT`（1 次）
- `batch_size:INT`（1 次）
- `show_help:STRING`（1 次）
- `GetImageSizeAndCount width:INT`（1 次）
- `GetImageSizeAndCount height:INT`（1 次）
- `count:INT`（1 次）
- `GetImageSizeAndCount 11 width:INT`（1 次）
- `GetImageSizeAndCount 11 height:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default", "qwen_image_vae.safetensors", "svdq-int4_r128-qwen-im`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
