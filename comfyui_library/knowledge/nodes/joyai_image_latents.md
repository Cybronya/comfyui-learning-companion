# JoyAI_Image_LATENTS

## 节点类型

`JoyAI_Image_LATENTS`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（7 次）
- `vae:VAE`（7 次）
- `seed:INT`（7 次）
- `width:INT`（7 次）
- `height:INT`（7 次）

## 输出

- `latent:LATENT`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1216048398, "fixed", 1024, 1024]`（4 次）
- `[1216048398, "fixed", 1024, 1536]`（2 次）
- `[1061052078, "randomize", 1024, 1024]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
