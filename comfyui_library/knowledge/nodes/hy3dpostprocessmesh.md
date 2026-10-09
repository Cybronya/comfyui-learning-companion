# Hy3DPostprocessMesh

## 节点类型

`Hy3DPostprocessMesh`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `trimesh:TRIMESH`（2 次）
- `remove_floaters:BOOLEAN`（2 次）
- `remove_degenerate_faces:BOOLEAN`（2 次）
- `reduce_faces:BOOLEAN`（2 次）
- `max_facenum:INT`（2 次）
- `smooth_normals:BOOLEAN`（2 次）
- `mask:MASK`（2 次）

## 输出

- `trimesh:TRIMESH`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, true, true, 50000, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
