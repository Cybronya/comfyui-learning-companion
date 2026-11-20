# Trellis2SparseGenerator

## 节点类型

`Trellis2SparseGenerator`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:TRELLIS2PIPELINE`（1 次）
- `image_cond:IMAGE_COND`（1 次）
- `seed:INT`（1 次）
- `sparse_structure_steps:INT`（1 次）
- `sparse_structure_guidance_strength:FLOAT`（1 次）
- `sparse_structure_guidance_rescale:FLOAT`（1 次）
- `sparse_structure_rescale_t:FLOAT`（1 次）
- `sparse_structure_sampler:COMBO`（1 次）
- `sparse_structure_resolution:INT`（1 次）
- `sparse_structure_guidance_interval_start:FLOAT`（1 次）

## 输出

- `coords:COORDS`（1 次）
- `sparse_structure_resolution:INT`（1 次）
- `pipeline:TRELLIS2PIPELINE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[12345, "fixed", 12, 7.5, 0.01, 5, "heun", 32, 0.1, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
