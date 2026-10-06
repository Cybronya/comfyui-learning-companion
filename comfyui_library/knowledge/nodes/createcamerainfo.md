# CreateCameraInfo

## 节点类型

`CreateCameraInfo`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `mode:COMFY_DYNAMICCOMBO_V3`（3 次）
- `mode.yaw:FLOAT`（3 次）
- `mode.pitch:FLOAT`（3 次）
- `mode.distance:FLOAT`（3 次）
- `target_x:FLOAT`（3 次）
- `target_y:FLOAT`（3 次）
- `target_z:FLOAT`（3 次）
- `roll:FLOAT`（3 次）
- `fov:FLOAT`（3 次）
- `zoom:FLOAT`（3 次）

## 输出

- `camera_info:LOAD3D_CAMERA`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["orbit", 35, 15, 2.5, 0, 0, 0, 0, 50, 1, "perspective"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
