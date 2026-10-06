# ImageScaleToTotalPixels

## 节点类型

`ImageScaleToTotalPixels`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 62 个 workflow 中。

## 输入

- `image:IMAGE`（116 次）
- `upscale_method:COMBO`（116 次）
- `megapixels:FLOAT`（116 次）
- `resolution_steps:INT`（116 次）

## 输出

- `IMAGE:IMAGE`（116 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["lanczos", 1, 32]`（35 次）
- `["lanczos", 1, 1]`（35 次）
- `["lanczos", 0.6000000000000001, 32]`（8 次）
- `["lanczos", 2.0000000000000004, 32]`（8 次）
- `["lanczos", 0.30000000000000004, 1]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
