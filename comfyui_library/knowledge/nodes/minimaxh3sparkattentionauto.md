# MiniMaxH3SparkAttentionAuto

## 节点类型

`MiniMaxH3SparkAttentionAuto`

## 分类

Optimization

## 作用

注意力/加速优化节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `enabled:BOOLEAN`（2 次）
- `steps:INT`（2 次）
- `warmup_mode:COMBO`（2 次）
- `warmup_ratio:FLOAT`（2 次）
- `warmup_steps:INT`（2 次）
- `topk_mode:COMBO`（2 次）
- `topk_ratio:FLOAT`（2 次）
- `topk_blocks:INT`（2 次）
- `dense_layers:INT`（2 次）

## 输出

- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, 4, "warmup_ratio", 0, 4, "topk_ratio", 0.30000000000000004, 228, 2, 12288, true, "query", "q_reuse_k"]`（1 次）
- `[true, 28, "warmup_steps", 0.2, 2, "topk_ratio", 0.30000000000000004, 228, 2, 12288, true, "query", "q_reuse_k"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
