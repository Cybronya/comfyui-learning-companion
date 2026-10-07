# Image Chromatic Aberration

## 节点类型

`Image Chromatic Aberration`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `red_offset:INT`（1 次）
- `green_offset:INT`（1 次）
- `blue_offset:INT`（1 次）
- `intensity:FLOAT`（1 次）
- `fade_radius:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 2, 0.4, 20]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
