# UntwistingRoPE

## 节点类型

`UntwistingRoPE`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `rf_inversion:LATENT`（3 次）
- `unofficial_extensions:UNTWISTING_ROPE_EXTENSIONS`（3 次）
- `beta:FLOAT`（3 次）
- `high_scale_start:FLOAT`（3 次）
- `high_scale_end:FLOAT`（3 次）
- `low_scale_start:FLOAT`（3 次）
- `low_scale_end:FLOAT`（3 次）
- `adain_strength:FLOAT`（3 次）
- `blocks:STRING`（3 次）

## 输出

- `model:MODEL`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[10, 0.9, 0, 1, 5, 0.5, "19-31", true]`（1 次）
- `[25, 0.95, 0, 1, 4, 0.5, "0-999", true]`（1 次）
- `[20.000000000000004, 1, 0, 1, 1.4, 0.5, "0-999", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
