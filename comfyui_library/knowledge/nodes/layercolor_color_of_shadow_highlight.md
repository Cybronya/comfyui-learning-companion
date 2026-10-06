# LayerColor: Color of Shadow & Highlight

## 节点类型

`LayerColor: Color of Shadow & Highlight`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `mask:MASK`（4 次）
- `shadow_brightness:FLOAT`（4 次）
- `shadow_saturation:FLOAT`（4 次）
- `shadow_hue:INT`（4 次）
- `shadow_level_offset:INT`（4 次）
- `shadow_range:FLOAT`（4 次）
- `highlight_brightness:FLOAT`（4 次）
- `highlight_saturation:FLOAT`（4 次）
- `highlight_hue:INT`（4 次）

## 输出

- `image:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 1, -1, 0, 0.010000000000000002, 1.1000000000000003, 1, 1, ["701", 0], 0.10000000000000002]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
