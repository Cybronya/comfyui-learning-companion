# LayerUtility: ImageShift

## 节点类型

`LayerUtility: ImageShift`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `shift_x:INT`（1 次）
- `shift_y:INT`（1 次）
- `cyclic:BOOLEAN`（1 次）
- `background_color:STRING`（1 次）
- `border_mask_width:INT`（1 次）
- `border_mask_blur:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `border_mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, true, "#000000", 50, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
