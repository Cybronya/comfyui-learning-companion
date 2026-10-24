# GearColorGrade

## 节点类型

`GearColorGrade`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `hdr_linear:IMAGE`（1 次）
- `sdr_reference:IMAGE`（1 次）
- `exposure:FLOAT`（1 次）
- `tone_map:COMBO`（1 次）
- `soft_clip:FLOAT`（1 次）
- `temperature:FLOAT`（1 次）
- `tint:FLOAT`（1 次）
- `lift_r:FLOAT`（1 次）
- `lift_g:FLOAT`（1 次）
- `lift_b:FLOAT`（1 次）

## 输出

- `graded_display:IMAGE`（1 次）
- `graded_linear:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "ACES Fitted", 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0.18, 0, 0, 1, 0, 0, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
