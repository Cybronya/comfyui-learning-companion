# ImageWatermark

## 节点类型

`ImageWatermark`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `text:STRING`（1 次）
- `font_file:STRING`（1 次）
- `angle:INT`（1 次）
- `red:INT`（1 次）
- `green:INT`（1 次）
- `blue:INT`（1 次）
- `opacity:FLOAT`（1 次）
- `size:INT`（1 次）
- `space:INT`（1 次）

## 输出

- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["SHS-SY", "", 30, 255, 255, 255, 0.2, 50, 75, "None", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
