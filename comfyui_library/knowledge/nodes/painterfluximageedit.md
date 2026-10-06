# PainterFluxImageEdit

## 节点类型

`PainterFluxImageEdit`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `clip:CLIP`（5 次）
- `vae:VAE`（5 次）
- `image1:IMAGE`（5 次）
- `image2:IMAGE`（5 次）
- `image3:IMAGE`（5 次）
- `image1_mask:MASK`（5 次）
- `prompt:STRING`（5 次）
- `width:INT`（5 次）
- `height:INT`（5 次）

## 输出

- `positive:CONDITIONING`（5 次）
- `negative:CONDITIONING`（5 次）
- `latent:LATENT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 1024, 1024]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
