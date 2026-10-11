# workflow>load image01

## 节点类型

`workflow>load image01`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vae:VAE`（1 次）
- `conditioning:CONDITIONING`（1 次）
- `入参 1｜模特全身照 · 负向图像参考 conditioning:CONDITIONING`（1 次）
- `image:COMBO`（1 次）
- `upload:IMAGEUPLOAD`（1 次）
- `upscale_method:COMBO`（1 次）
- `megapixels:FLOAT`（1 次）
- `resolution_steps:INT`（1 次）
- `ReferenceLatent conditioning:CONDITIONING`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `MASK:MASK`（1 次）
- `入参 1｜模特全身照 · Lanczos 缩放｜1.5 MP · 16 对齐 IMAGE:IMAGE`（1 次）
- `CONDITIONING:CONDITIONING`（1 次）
- `入参 1｜模特全身照 · 负向图像参考 CONDITIONING:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["beb954501c7df8adc14df7daca0586952ceb85ef1b46689aac6a658363e88d73.png", "image", "lanczos", 1.5, 16]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
