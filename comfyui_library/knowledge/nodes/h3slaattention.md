# H3SLAAttention

## 节点类型

`H3SLAAttention`

## 分类

Optimization

## 作用

注意力/加速优化节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `sparsity_ratio:FLOAT`（1 次）
- `block_size:COMBO`（1 次）
- `min_seq_len:INT`（1 次）
- `dense_last_steps:INT`（1 次）
- `protect_audio:BOOLEAN`（1 次）
- `enabled:BOOLEAN`（1 次）
- `dense_steps:STRING`（1 次）
- `dense_backend:COMBO`（1 次）
- `disable_fp16_accum:BOOLEAN`（1 次）

## 输出

- `MODEL:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.9000000000000001, "64", 8192, 0, true, true, "1", "comfy_kitchen", true, false, "Off", false, true, "comfy_kitchen"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
