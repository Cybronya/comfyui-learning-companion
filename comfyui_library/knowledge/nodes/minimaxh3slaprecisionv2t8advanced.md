# MiniMaxH3SLAPrecisionV2T8Advanced

## 节点类型

`MiniMaxH3SLAPrecisionV2T8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `sigmas:SIGMAS`（1 次）
- `schedule_policy:COMBO`（1 次）
- `sparsity_ratio:FLOAT`（1 次）
- `block_size:COMBO`（1 次）
- `min_seq_len:INT`（1 次）
- `dense_last_steps:INT`（1 次）
- `protect_audio:BOOLEAN`（1 次）
- `dense_steps:STRING`（1 次）
- `dense_backend:COMBO`（1 次）

## 输出

- `model:MODEL`（1 次）
- `runtime:MINIMAX_H3_SLA_PRECISION_V2_RUNTIME`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["recommended_8nfe_12v_3a", 0.9, "32", 8192, 1, true, "0", "comfy_kitchen", true, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
