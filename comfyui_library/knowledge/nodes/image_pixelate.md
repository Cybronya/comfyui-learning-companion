# Image Pixelate

## 节点类型

`Image Pixelate`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `color_palettes:LIST`（1 次）
- `pixelation_size:FLOAT`（1 次）
- `num_colors:FLOAT`（1 次）
- `init_mode:COMBO`（1 次）
- `max_iterations:FLOAT`（1 次）
- `dither:COMBO`（1 次）
- `dither_mode:COMBO`（1 次）
- `color_palette_mode:COMBO`（1 次）
- `reverse_palette:COMBO`（1 次）

## 输出

- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[16, 100, "k-means++", 100, "False", "FloydSteinberg", "Brightness", "False"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
