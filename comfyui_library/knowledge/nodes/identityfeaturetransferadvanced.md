# IdentityFeatureTransferAdvanced

## 节点类型

`IdentityFeatureTransferAdvanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `subject_mask:MASK`（1 次）
- `reference_index:INT`（1 次）
- `mode:COMBO`（1 次）
- `top_k_percent:FLOAT`（1 次）
- `double_enable:BOOLEAN`（1 次）
- `double_strength:FLOAT`（1 次）
- `double_start:INT`（1 次）
- `double_end:INT`（1 次）
- `single_enable:BOOLEAN`（1 次）

## 输出

- `MODEL:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "cosine_pull", 0.25, true, 0.25, 0, 7, true, 0.3, 0, 23, "flat", 0.02, 0.95]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
