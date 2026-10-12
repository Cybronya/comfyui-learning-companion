# workflow>process

## 节点类型

`workflow>process`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `ref_image:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `TextEncodeQwenImageEditPlus image2:IMAGE`（1 次）
- `TextEncodeQwenImageEditPlus image3:IMAGE`（1 次）
- `value:INT`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）

## 输出

- `mask:MASK`（1 次）
- `original_size:BOX`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `COMBO:*`（1 次）
- `output:*`（1 次）
- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, "qwen_2.5_vl_7b_fp8_scaled.safetensors", "qwen_image", "default", "qwen_image_vae.safetensors", "Qwen-Image-Edit-`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
