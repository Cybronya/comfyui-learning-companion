# TS_ImageToSVGStringColor_Vtracer

## 节点类型

`TS_ImageToSVGStringColor_Vtracer`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `hierarchical:COMBO`（1 次）
- `mode:COMBO`（1 次）
- `filter_speckle:INT`（1 次）
- `color_precision:INT`（1 次）
- `layer_difference:INT`（1 次）
- `corner_threshold:INT`（1 次）
- `length_threshold:FLOAT`（1 次）
- `max_iterations:INT`（1 次）
- `splice_threshold:INT`（1 次）

## 输出

- `STRING:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["stacked", "spline", 4, 6, 16, 60, 4, 10, 45, 3]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
