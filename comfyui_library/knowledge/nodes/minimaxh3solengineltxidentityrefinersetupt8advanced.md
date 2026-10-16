# MiniMaxH3SolEngineLTXIdentityRefinerSetupT8Advanced

## 节点类型

`MiniMaxH3SolEngineLTXIdentityRefinerSetupT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `enabled:BOOLEAN`（1 次）
- `schedule_mode:COMBO`（1 次）
- `manual_sigmas:STRING`（1 次）
- `attention_backend:COMBO`（1 次）
- `min_tokens:INT`（1 次）
- `kernel_precision:COMBO`（1 次）
- `verbose:BOOLEAN`（1 次）

## 输出

- `model:MODEL`（1 次）
- `sampler:SAMPLER`（1 次）
- `sigmas:SIGMAS`（1 次）
- `refiner_lora_strength:FLOAT`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "manual_exp", "0.5, 0.412, 0.350, 0", "auto_sol_attn_conservative_exp", 4096, "bf16_official", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
