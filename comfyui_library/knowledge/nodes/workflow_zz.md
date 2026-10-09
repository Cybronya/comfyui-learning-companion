# workflow>zz

## 节点类型

`workflow>zz`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `遮罩:MASK`（1 次）
- `channel:COMBO`（1 次）
- `expand:INT`（1 次）
- `incremental_expandrate:FLOAT`（1 次）
- `tapered_corners:BOOLEAN`（1 次）
- `flip_input:BOOLEAN`（1 次）
- `blur_radius:FLOAT`（1 次）
- `lerp_alpha:FLOAT`（1 次）
- `decay_factor:FLOAT`（1 次）
- `fill_holes:BOOLEAN`（1 次）

## 输出

- `遮罩:MASK`（1 次）
- `反转遮罩:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["red", 2, 0, true, false, 1, 1, 1, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
