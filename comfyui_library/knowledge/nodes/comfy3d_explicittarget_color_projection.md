# [Comfy3D] ExplicitTarget Color Projection

## 节点类型

`[Comfy3D] ExplicitTarget Color Projection`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `mesh:MESH`（1 次）
- `reference_images:IMAGE`（1 次）
- `reference_masks:MASK`（1 次）
- `reference_orbit_camera_poses:ORBIT_CAMPOSES`（1 次）
- `projection_resolution:INT`（1 次）
- `complete_unseen_rgb:BOOLEAN`（1 次）
- `render_orbit_camera_fovy:FLOAT`（1 次）
- `projection_weights:STRING`（1 次）
- `confidence_threshold:FLOAT`（1 次）
- `texture_projecton:BOOLEAN`（1 次）

## 输出

- `mesh:MESH`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, true, 47.5, "2.0, 0.2, 1.0, 0.2", 0.02, false, "Albedo"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
