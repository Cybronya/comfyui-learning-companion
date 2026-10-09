# VedaSparseAttention

## 节点类型

`VedaSparseAttention`

## 分类

Optimization

## 作用

注意力/加速优化节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `predictor:COMBO`（2 次）
- `generated_sparsity:STRING`（2 次）
- `reference_sparsity:STRING`（2 次）
- `full_attention_layers:STRING`（2 次）
- `full_attention_steps:STRING`（2 次）
- `verbose:BOOLEAN`（2 次）

## 输出

- `model:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["minimax_h3_t2va_veda_8nfe_600step_preview_fp8.safetensors", "90%", "90%", "", "", true, "Veda done, fell back to full `（1 次）
- `["minimax_h3_t2va_veda_8nfe_600step_preview_fp8.safetensors", "90%", "90%", "", "", false, "Veda done · Triton INT8 (SM8`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
