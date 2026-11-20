# PH3ImageConditioning

## 节点类型

`PH3ImageConditioning`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `clip:CLIP`（9 次）
- `vae:VAE`（9 次）
- `images.image_1:IMAGE`（9 次）
- `prompt:STRING`（9 次）
- `width:INT`（9 次）
- `height:INT`（9 次）
- `images.image_2:IMAGE`（1 次）
- `images.image_3:IMAGE`（1 次）
- `images.image_4:IMAGE`（1 次）
- `images.image_5:IMAGE`（1 次）

## 输出

- `positive:CONDITIONING`（9 次）
- `LATENT:LATENT`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 0, 0]`（9 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
