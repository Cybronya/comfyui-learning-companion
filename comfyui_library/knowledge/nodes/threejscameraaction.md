# ThreeJSCameraAction

## 节点类型

`ThreeJSCameraAction`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `action_type:COMBO`（4 次）
- `start_frame:INT`（4 次）
- `end_frame:INT`（4 次）
- `start_value:FLOAT`（4 次）
- `end_value:FLOAT`（4 次）
- `easing:COMBO`（4 次）

## 输出

- `camera_action:ACTION_SEGMENT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["roll (镜头旋转)", 20, 40, -10, 10, "linear"]`（1 次）
- `["roll (镜头旋转)", 40, 60, 10, -10, "linear"]`（1 次）
- `["roll (镜头旋转)", 0, 20, 0, -10, "linear"]`（1 次）
- `["roll (镜头旋转)", 60, 81, -10, 0, "linear"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
