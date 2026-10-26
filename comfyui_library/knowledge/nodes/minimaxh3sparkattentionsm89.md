# MiniMaxH3SparkAttentionSM89

## 节点类型

`MiniMaxH3SparkAttentionSM89`

## 分类

Optimization

## 作用

注意力/加速优化节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `model:MODEL`（6 次）
- `enabled:BOOLEAN`（6 次）
- `steps:INT`（6 次）
- `warmup_mode:COMBO`（6 次）
- `warmup_ratio:FLOAT`（6 次）
- `warmup_steps:INT`（6 次）
- `topk_mode:COMBO`（6 次）
- `topk_ratio:FLOAT`（6 次）
- `topk_blocks:INT`（6 次）
- `dense_layers:INT`（6 次）

## 输出

- `MODEL:MODEL`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 8, "warmup_steps", 0.2, 2, "topk_ratio", 0.2, 228, 0, 12288, true, "query", "q_reuse_k"]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
