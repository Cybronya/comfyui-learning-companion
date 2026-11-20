# ImageMerger

## 节点类型

`ImageMerger`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `images_1:IMAGE`（7 次）
- `images_2:IMAGE`（7 次）
- `divide_points:STRING`（5 次）
- `line_thickness:INT`（5 次）

## 输出

- `images:IMAGE`（7 次）
- `num_images:INT`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["(50%, 0);(50%, 100%)", 0]`（7 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
