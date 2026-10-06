# BlockSparseAttention

## 节点类型

`BlockSparseAttention`

## 分类

Optimization

## 作用

注意力/加速优化节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 20 个 workflow 中。

## 输入

- `model:MODEL`（20 次）
- `selection:COMFY_DYNAMICCOMBO_V3`（20 次）
- `selection.tau:FLOAT`（20 次）
- `start_percent:FLOAT`（20 次）
- `end_percent:FLOAT`（20 次）
- `dense_blocks:STRING`（20 次）
- `min_tokens:INT`（20 次）
- `extra_tokens:INT`（20 次）
- `sink_conditioning:COMBO`（20 次）
- `verbose:BOOLEAN`（20 次）

## 输出

- `model:MODEL`（20 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["sol-attn", 1.3, 0.2, 1, "", 12288, 256, "exact_kv_and_rows", true]`（19 次）
- `["sol-attn", 1.3, 0.2, 1, "", 12288, 256, "exact_kv_and_rows", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
