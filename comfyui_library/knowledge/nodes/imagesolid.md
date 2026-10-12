# ImageSolid

## 节点类型

`ImageSolid`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `reference_image:IMAGE`（1 次）
- `preset_size:COMBO`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `color:COLOR`（1 次）
- `alpha:FLOAT`（1 次）
- `invert:BOOLEAN`（1 次）
- `mask_opacity:FLOAT`（1 次）
- `divisible_by:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["custom", 752, 1392, "#FFFFFF", 1, false, 1, 8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
