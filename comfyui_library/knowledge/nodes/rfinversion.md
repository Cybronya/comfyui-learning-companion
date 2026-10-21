# RFInversion

## 节点类型

`RFInversion`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `reference_latent:LATENT`（3 次）
- `ref_conditioning:CONDITIONING`（3 次）
- `rf_mode:COMBO`（3 次）
- `gamma:FLOAT`（3 次）
- `gamma_curve:FLOAT`（3 次）
- `norm_strength:FLOAT`（3 次）
- `pmi_alpha:FLOAT`（3 次）
- `verbose:BOOLEAN`（3 次）

## 输出

- `model:MODEL`（3 次）
- `rf_inversion:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["rf_gamma", 0.5, 1, 1, 0, false]`（2 次）
- `["rf_gamma", 0.5, 2, 1, 0, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
