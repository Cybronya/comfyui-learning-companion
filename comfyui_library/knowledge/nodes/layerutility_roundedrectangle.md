# LayerUtility: RoundedRectangle

## 节点类型

`LayerUtility: RoundedRectangle`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `object_mask:MASK`（1 次）
- `crop_box:BOX`（1 次）
- `rounded_rect_radius:INT`（1 次）
- `anti_aliasing:INT`（1 次）
- `top:FLOAT`（1 次）
- `bottom:FLOAT`（1 次）
- `left:FLOAT`（1 次）
- `right:FLOAT`（1 次）
- `detect:COMBO`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[30, 5, 8, 8, 8, 8, "mask_area", 8, 8, 8, 8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
