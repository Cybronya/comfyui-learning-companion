# SpectrumApplyMiniMaxH3

## 节点类型

`SpectrumApplyMiniMaxH3`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `enabled:BOOLEAN`（2 次）
- `blend_weight:FLOAT`（2 次）
- `degree:INT`（2 次）
- `ridge_lambda:FLOAT`（2 次）
- `window_size:FLOAT`（2 次）
- `flex_window:FLOAT`（2 次）
- `warmup_steps:INT`（2 次）
- `tail_actual_steps:INT`（2 次）
- `max_history:INT`（2 次）

## 输出

- `model:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 0.5, 1, 0.1, 2, 0.75, 1, 1, 8, false, "system_ram", true, false, false, true, 0, "system_ram", "off", 0.65, false`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
