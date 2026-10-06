# SolAttnMiniMax

## 节点类型

`SolAttnMiniMax`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 22 个 workflow 中。

## 输入

- `model:MODEL`（22 次）
- `tau_profile:STRING`（22 次）
- `tau:FLOAT`（22 次）
- `start_percent:FLOAT`（22 次）
- `end_percent:FLOAT`（22 次）
- `min_tokens:INT`（22 次）
- `sink_conditioning:COMBO`（22 次）
- `morton:BOOLEAN`（22 次）
- `morton_curve:COMBO`（22 次）
- `centroid_tail:BOOLEAN`（22 次）

## 输出

- `MODEL:MODEL`（22 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1.3, 0.2, 0.9, 12288, "exact_kv_and_rows", false, "2d_frame", true, 0, false, false, ""]`（22 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
