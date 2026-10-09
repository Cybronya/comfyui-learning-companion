# Hy3DCameraConfig

## 节点类型

`Hy3DCameraConfig`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `camera_azimuths:STRING`（2 次）
- `camera_elevations:STRING`（2 次）
- `view_weights:STRING`（2 次）
- `camera_distance:FLOAT`（2 次）
- `ortho_scale:FLOAT`（2 次）

## 输出

- `camera_config:HY3DCAMERA`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["0, 90, 180, 270, 0, 180", "0, 0, 0, 0, 90, -90", "1, 0.1, 0.5, 0.1, 0.05, 0.05", 1.45, 1.2]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
