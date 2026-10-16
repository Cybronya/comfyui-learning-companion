# Hy3DRenderSingleView

## 节点类型

`Hy3DRenderSingleView`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `trimesh:TRIMESH`（1 次）
- `render_type:COMBO`（1 次）
- `render_size:INT`（1 次）
- `camera_type:COMBO`（1 次）
- `camera_distance:FLOAT`（1 次）
- `pan_x:FLOAT`（1 次）
- `pan_y:FLOAT`（1 次）
- `ortho_scale:FLOAT`（1 次）
- `azimuth:FLOAT`（1 次）
- `elevation:FLOAT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["normal", 1024, "orth", 1.45, 0, 0, 1.2, 0, 0, "128, 128, 255"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
