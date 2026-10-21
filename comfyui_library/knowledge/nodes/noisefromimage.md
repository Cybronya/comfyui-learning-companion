# NoiseFromImage+

## 节点类型

`NoiseFromImage+`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `noise_mask:IMAGE`（1 次）
- `noise_strenght:FLOAT`（1 次）
- `noise_size:FLOAT`（1 次）
- `color_noise:FLOAT`（1 次）
- `mask_strength:FLOAT`（1 次）
- `mask_scale_diff:FLOAT`（1 次）
- `mask_contrast:FLOAT`（1 次）
- `saturation:FLOAT`（1 次）
- `contrast:FLOAT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 0.1, 0, 1, 0, 1, 1, 1, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
