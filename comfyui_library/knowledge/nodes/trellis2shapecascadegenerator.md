# Trellis2ShapeCascadeGenerator

## 节点类型

`Trellis2ShapeCascadeGenerator`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:TRELLIS2PIPELINE`（1 次）
- `image_cond:IMAGE_COND`（1 次）
- `shape_slat:SHAPE_SLAT`（1 次）
- `from_resolution:INT`（1 次）
- `to_resolution:COMBO`（1 次）
- `sparse_structure_resolution:INT`（1 次）
- `max_num_tokens:INT`（1 次）
- `shape_steps:INT`（1 次）
- `shape_guidance_strength:FLOAT`（1 次）
- `shape_guidance_rescale:FLOAT`（1 次）

## 输出

- `shape_slat:SHAPE_SLAT`（1 次）
- `resolution:INT`（1 次）
- `pipeline:TRELLIS2PIPELINE`（1 次）
- `num_tokens:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 1024, 0, 999999, 12, 7.5, 0.01, 3, "heun", 0.1, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
