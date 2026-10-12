# ADE_CameraPoseAdvanced

## 节点类型

`ADE_CameraPoseAdvanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prev_poses:CAMERACTRL_POSES`（4 次）
- `motion_type1:COMBO`（4 次）
- `strength1:FLOAT`（4 次）
- `motion_type2:COMBO`（4 次）
- `strength2:FLOAT`（4 次）
- `motion_type3:COMBO`（4 次）
- `strength3:FLOAT`（4 次）
- `motion_type4:COMBO`（4 次）
- `strength4:FLOAT`（4 次）
- `motion_type5:COMBO`（4 次）

## 输出

- `CAMERACTRL_POSES:CAMERACTRL_POSES`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Roll Anticlockwise", 2.0000000000000004, "Zoom Out", 1, "Static", 1, "Static", 1, "Static", 1, "Static", 1, 0.50000000`（1 次）
- `["Tilt Left", 1, "Zoom Out", 1, "Static", 1, "Static", 1, "Static", 1, "Static", 1, 0.5000000000000001, 121]`（1 次）
- `["Tilt Right", 1, "Zoom In", 1, "Pan Right", 1, "Static", 1, "Static", 1, "Static", 1, 0.5000000000000001, 121]`（1 次）
- `["Roll Clockwise", 1, "Zoom Out", 2.0000000000000004, "Static", 1, "Static", 1, "Static", 1, "Static", 1, 0.800000000000`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
