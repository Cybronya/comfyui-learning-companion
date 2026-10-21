# ImpactMakeTileSEGS

## 节点类型

`ImpactMakeTileSEGS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `filter_in_segs_opt:SEGS`（1 次）
- `filter_out_segs_opt:SEGS`（1 次）
- `bbox_size:INT`（1 次）
- `crop_factor:FLOAT`（1 次）
- `min_overlap:INT`（1 次）
- `filter_segs_dilation:INT`（1 次）
- `mask_irregularity:FLOAT`（1 次）
- `irregular_mask_mode:COMBO`（1 次）

## 输出

- `SEGS:SEGS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[872, 1.1, 16, 20, 0, "Reuse fast"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
