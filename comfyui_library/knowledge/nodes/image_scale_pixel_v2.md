# image_scale_pixel_v2

## 节点类型

`image_scale_pixel_v2`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（2 次）
- `masks:MASK`（2 次）
- `option:SO`（2 次）
- `TotalPixels:FLOAT`（2 次）
- `alignment:COMBO`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.10000000000000002, "64(sd/kontext/wan)"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
