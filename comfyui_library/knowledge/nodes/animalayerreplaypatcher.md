# AnimaLayerReplayPatcher

## 节点类型

`AnimaLayerReplayPatcher`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `enable_replay:BOOLEAN`（1 次）
- `block_indices:STRING`（1 次）
- `denoise_start_pct:FLOAT`（1 次）
- `denoise_end_pct:FLOAT`（1 次）
- `enable_spectrum:BOOLEAN`（1 次）
- `spectrum_w:FLOAT`（1 次）
- `spectrum_m:INT`（1 次）
- `spectrum_lam:FLOAT`（1 次）
- `spectrum_warmup_steps:INT`（1 次）

## 输出

- `MODEL:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "3,4,5", 0.5, 1, false, 0.2, 16, 0.5, 6, 2, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
