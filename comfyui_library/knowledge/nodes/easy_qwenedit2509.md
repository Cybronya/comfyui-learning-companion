# Easy_QwenEdit2509

## 节点类型

`Easy_QwenEdit2509`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `vae:VAE`（1 次）
- `image1:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `latent_image:IMAGE`（1 次）
- `latent_mask:MASK`（1 次）
- `auto_resize:COMBO`（1 次）
- `vl_size:INT`（1 次）
- `prompt:STRING`（1 次）

## 输出

- `positive:CONDITIONING`（1 次）
- `zero_negative:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["crop", 384, "transform the image to realistic photograph\n", "Describe the key features of the input image (color, sha`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
