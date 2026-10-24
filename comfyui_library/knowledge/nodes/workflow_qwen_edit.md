# workflow>QWEN-EDIT

## 节点类型

`workflow>QWEN-EDIT`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `ImageScaleToTotalPixels image:IMAGE`（2 次）
- `image3:IMAGE`（2 次）
- `TextEncodeQwenImageEditPlus image3:IMAGE`（2 次）
- `clip_name:COMBO`（2 次）
- `type:COMBO`（2 次）
- `device:COMBO`（2 次）
- `vae_name:COMBO`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）

## 输出

- `width:INT`（2 次）
- `height:INT`（2 次）
- `upscale_factor:FLOAT`（2 次）
- `batch_size:INT`（2 次）
- `show_help:STRING`（2 次）
- `GetImageSizeAndCount width:INT`（2 次）
- `GetImageSizeAndCount height:INT`（2 次）
- `count:INT`（2 次）
- `GetImageSizeAndCount 10 width:INT`（2 次）
- `GetImageSizeAndCount 10 height:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default", "qwen_image_vae.safetensors", 1024, 1024, "16:9 lands`（1 次）
- `["qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default", "qwen_image_vae.safetensors", 1024, 1024, "16:9 lands`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
