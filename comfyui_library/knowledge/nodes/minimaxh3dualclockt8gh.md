# MiniMaxH3DualClockT8GH

## 节点类型

`MiniMaxH3DualClockT8GH`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `av_latent:LATENT`（1 次）
- `steps:INT`（1 次）
- `shift_video:FLOAT`（1 次）
- `shift_audio:FLOAT`（1 次）
- `sampler_name:COMBO`（1 次）
- `scheduler:COMBO`（1 次）

## 输出

- `model:MODEL`（1 次）
- `sampler:SAMPLER`（1 次）
- `sigmas:SIGMAS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[8, 12, 3, "dual_clock_euler", "native_flow"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
