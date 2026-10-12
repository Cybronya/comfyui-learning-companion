# ADE_CameraPoseCombo

## 节点类型

`ADE_CameraPoseCombo`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `prev_poses:CAMERACTRL_POSES`（2 次）
- `motion_type1:COMBO`（2 次）
- `motion_type2:COMBO`（2 次）
- `motion_type3:COMBO`（2 次）
- `motion_type4:COMBO`（2 次）
- `motion_type5:COMBO`（2 次）
- `motion_type6:COMBO`（2 次）
- `speed:FLOAT`（2 次）
- `frame_length:INT`（2 次）

## 输出

- `CAMERACTRL_POSES:CAMERACTRL_POSES`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Zoom Out", "Tilt Right", "Tilt Down", "Static", "Static", "Static", 0.2, 81]`（1 次）
- `["Zoom Out", "Tilt Left", "Static", "Static", "Static", "Static", 0.2, 81]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
