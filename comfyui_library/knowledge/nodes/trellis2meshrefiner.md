# Trellis2MeshRefiner

## 节点类型

`Trellis2MeshRefiner`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:TRELLIS2PIPELINE`（1 次）
- `trimesh:TRIMESH`（1 次）
- `image:IMAGE`（1 次）
- `seed:INT`（1 次）
- `resolution:COMBO`（1 次）
- `shape_steps:INT`（1 次）
- `shape_guidance_strength:FLOAT`（1 次）
- `shape_guidance_rescale:FLOAT`（1 次）
- `shape_rescale_t:FLOAT`（1 次）
- `texture_steps:INT`（1 次）

## 输出

- `mesh:MESHWITHVOXEL`（1 次）
- `bvh:BVH`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[12345, "fixed", 1536, 50, 6.5, 0, 4, 25, 3, 0.2, 3, 999999, false, 16, 0.1, 1, 0, 0.9, true, 4, "euler"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
