# ImageScaleByAspectRatio_UTK

## 节点类型

`ImageScaleByAspectRatio_UTK`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `proportional_width:INT`（1 次）
- `proportional_height:INT`（1 次）
- `fit:COMBO`（1 次）
- `method:COMBO`（1 次）
- `round_to_multiple:COMBO`（1 次）
- `scale_to_side:COMBO`（1 次）
- `scale_to_length:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `original_size:BOX`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["16:9", 1, 1, "letterbox", "lanczos", "8", "total_pixel(kilo pixel)", 2000, "#000000"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
