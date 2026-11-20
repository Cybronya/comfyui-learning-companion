# Trellis2MeshWithVoxelAdvancedGenerator

## 节点类型

`Trellis2MeshWithVoxelAdvancedGenerator`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `pipeline:TRELLIS2PIPELINE`（2 次）
- `image:IMAGE`（2 次）
- `seed:INT`（2 次）
- `pipeline_type:COMBO`（2 次）
- `sparse_structure_steps:INT`（2 次）
- `sparse_structure_guidance_strength:FLOAT`（2 次）
- `sparse_structure_guidance_rescale:FLOAT`（2 次）
- `sparse_structure_rescale_t:FLOAT`（2 次）
- `shape_steps:INT`（2 次）
- `shape_guidance_strength:FLOAT`（2 次）

## 输出

- `mesh:MESHWITHVOXEL`（2 次）
- `bvh:BVH`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[123456, "fixed", "512", 12, 6.5, 0.2, 4, 12, 6.5, 0.2, 4, 12, 3, 0.2, 3, 999999, 4, 32, false, 0.1, 1, 0.1, 1, 0, 0.9, `（1 次）
- `[12345, "fixed", "1024_cascade", 50, 6.5, 0, 4, 50, 6.5, 0, 4, 12, 3, 0.2, 3, 999999, 4, 32, false, 0.1, 1, 0.1, 1, 0, 0`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
