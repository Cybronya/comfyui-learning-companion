# SolAttnPatch

## 节点类型

`SolAttnPatch`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `tau_profile:STRING`（3 次）
- `tau:FLOAT`（3 次）
- `start_percent:FLOAT`（3 次）
- `end_percent:FLOAT`（3 次）
- `min_tokens:INT`（3 次）
- `int8_qk:BOOLEAN`（3 次）
- `sink_conditioning:COMBO`（3 次）
- `morton:BOOLEAN`（3 次）
- `morton_curve:COMBO`（3 次）

## 输出

- `MODEL:MODEL`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1.2, 0.2, 0.9, 4096, false, "exact_kv", false, "3d", false, false, false, ""]`（2 次）
- `[1.2, 0.2, 0.9, 4096, false, "exact_kv", true, "3d", false, false, false, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
