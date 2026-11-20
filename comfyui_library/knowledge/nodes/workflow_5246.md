# workflow>遮罩块

## 节点类型

`workflow>遮罩块`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `遮罩:MASK`（2 次）
- `combined:BOOLEAN`（2 次）
- `crop_factor:FLOAT`（2 次）
- `bbox_fill:BOOLEAN`（2 次）
- `drop_size:INT`（2 次）
- `contour_fill:BOOLEAN`（2 次）
- `block_size:INT`（2 次）
- `device:COMBO`（2 次）

## 输出

- `mask:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, 3, false, 10, false, 24, "cpu"]`（1 次）
- `[false, 3, false, 10, false, 8, "cpu"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
