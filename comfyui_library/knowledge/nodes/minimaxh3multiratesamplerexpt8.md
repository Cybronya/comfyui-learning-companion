# MiniMaxH3MultiRateSamplerEXPT8

## 节点类型

`MiniMaxH3MultiRateSamplerEXPT8`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `av_latent:LATENT`（3 次）
- `video_steps:INT`（3 次）
- `audio_steps:INT`（3 次）
- `shift_video:FLOAT`（3 次）
- `shift_audio:FLOAT`（3 次）

## 输出

- `model:MODEL`（3 次）
- `sampler:SAMPLER`（3 次）
- `sigmas:SIGMAS`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[8, 10, 12, 3]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
