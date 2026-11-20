# Trellis2UnWrapAndRasterizer

## 节点类型

`Trellis2UnWrapAndRasterizer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `mesh:MESHWITHVOXEL`（1 次）
- `bvh:BVH`（1 次）
- `mesh_cluster_threshold_cone_half_angle_rad:FLOAT`（1 次）
- `mesh_cluster_refine_iterations:INT`（1 次）
- `mesh_cluster_global_iterations:INT`（1 次）
- `mesh_cluster_smooth_strength:INT`（1 次）
- `texture_size:INT`（1 次）
- `texture_alpha_mode:COMBO`（1 次）
- `double_side_material:BOOLEAN`（1 次）
- `bake_on_vertices:BOOLEAN`（1 次）

## 输出

- `trimesh:TRIMESH`（1 次）
- `base_color_texture:IMAGE`（1 次）
- `metallic_roughness_texture:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[60, 0, 1, 1, 4096, "OPAQUE", false, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
