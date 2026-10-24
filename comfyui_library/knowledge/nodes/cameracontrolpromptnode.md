# CameraControlPromptNode

## 节点类型

`CameraControlPromptNode`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `move_horizontal:COMBO`（22 次）
- `move_vertical:COMBO`（22 次）
- `move_forward:COMBO`（22 次）
- `rotate:INT`（22 次）
- `view_top_down:BOOLEAN`（22 次）
- `view_wide_angle:BOOLEAN`（22 次）
- `view_close_up:BOOLEAN`（22 次）
- `view_bottom_up:BOOLEAN`（22 次）

## 输出

- `prompt:STRING`（22 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["none", "none", "no", 90, false, false, false, false]`（2 次）
- `["right", "up", "no", 45, true, false, false, false]`（2 次）
- `["left", "up", "no", -45, true, false, false, false]`（2 次）
- `["right", "none", "yes", 45, false, false, false, false]`（2 次）
- `["left", "none", "yes", -45, false, false, false, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
