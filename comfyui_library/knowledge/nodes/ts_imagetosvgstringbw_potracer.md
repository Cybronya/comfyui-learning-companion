# TS_ImageToSVGStringBW_Potracer

## 节点类型

`TS_ImageToSVGStringBW_Potracer`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `threshold:INT`（1 次）
- `input_foreground:COMBO`（1 次）
- `turnpolicy:COMBO`（1 次）
- `turdsize:INT`（1 次）
- `corner_threshold:FLOAT`（1 次）
- `zero_sharp_corners:BOOLEAN`（1 次）
- `opttolerance:FLOAT`（1 次）
- `optimize_curve:BOOLEAN`（1 次）
- `foreground_color:STRING`（1 次）

## 输出

- `STRING:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[128, "Black on White", "minority", 2, 1, false, 0.2, true, "#000000", "#FFFFFF", "#FF0000", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
