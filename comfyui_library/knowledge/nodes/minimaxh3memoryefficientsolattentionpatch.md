# MiniMaxH3MemoryEfficientSolAttentionPatch

## 节点类型

`MiniMaxH3MemoryEfficientSolAttentionPatch`

## 分类

Optimization

## 作用

注意力/加速优化节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `enabled:BOOLEAN`（1 次）
- `tau:FLOAT`（1 次）
- `min_tokens:INT`（1 次）
- `strict:BOOLEAN`（1 次）
- `thresh_type:COMBO`（1 次）
- `int8_qk:BOOLEAN`（1 次）
- `int8_pv:BOOLEAN`（1 次）
- `sink_conditioning:COMBO`（1 次）
- `dense_blocks:STRING`（1 次）

## 输出

- `MODEL:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 1.3, 4096, false, "diag", false, false, "exact_kv", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
