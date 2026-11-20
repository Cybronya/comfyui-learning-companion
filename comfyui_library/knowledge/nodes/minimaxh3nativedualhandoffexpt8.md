# MiniMaxH3NativeDualHandoffEXPT8

## 节点类型

`MiniMaxH3NativeDualHandoffEXPT8`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `learned_latent:LATENT`（1 次）
- `highres_template:LATENT`（1 次）
- `positive:CONDITIONING`（1 次）
- `first_pass_steps:COMBO`（1 次）
- `second_audio_source:COMBO`（1 次）
- `second_audio_strength:FLOAT`（1 次）

## 输出

- `av_latent:LATENT`（1 次）
- `positive:CONDITIONING`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["4", "auto", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
