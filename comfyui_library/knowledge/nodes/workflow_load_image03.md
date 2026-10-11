# workflow>load image03

## 节点类型

`workflow>load image03`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vae:VAE`（1 次）
- `conditioning:CONDITIONING`（1 次）
- `入参 3｜下装参考图 · 负向图像参考 conditioning:CONDITIONING`（1 次）
- `image:COMBO`（1 次）
- `upload:IMAGEUPLOAD`（1 次）
- `upscale_method:COMBO`（1 次）
- `megapixels:FLOAT`（1 次）
- `resolution_steps:INT`（1 次）
- `ReferenceLatent conditioning:CONDITIONING`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `MASK:MASK`（1 次）
- `CONDITIONING:CONDITIONING`（1 次）
- `入参 3｜下装参考图 · 负向图像参考 CONDITIONING:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["7c38419c32df53de49240b051eef9c43b066e1b997e6133c2ca925745405c127.png", "image", "lanczos", 1.5, 16]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
