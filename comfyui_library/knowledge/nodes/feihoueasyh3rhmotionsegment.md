# FeiHouEasyH3RHMotionSegment

## 节点类型

`FeiHouEasyH3RHMotionSegment`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `h3_context:MINIMAX_H3_CONTEXT`（2 次）
- `shot_prompts:FEIHOU_H3_RH_PRODUCTION_SHOT`（2 次）
- `sampler_name:COMBO`（2 次）
- `scheduler:COMBO`（2 次）
- `steps:INT`（2 次）
- `first_steps:INT`（2 次）
- `shift_video:FLOAT`（2 次）
- `shift_audio:FLOAT`（2 次）
- `cfg:FLOAT`（2 次）

## 输出

- `noise:NOISE`（2 次）
- `guider:GUIDER`（2 次）
- `sampler:SAMPLER`（2 次）
- `sigmas:SIGMAS`（2 次）
- `latent:LATENT`（2 次）
- `motion_state:FEIHOU_H3_MOTION_STATE`（2 次）
- `video_vae:VAE`（2 次）
- `audio_vae:VAE`（2 次）
- `fps:FLOAT`（2 次）
- `h3_context:MINIMAX_H3_CONTEXT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["dual_clock_euler", "simple", 9, 4, 12, 3, 1, "送入模型", "帧窗口", true, "141 帧 · 5.88 秒", "22", "226 帧 · 9.42 秒", "68"]`（1 次）
- `["dual_clock_euler", "simple", 9, 4, 12, 3, 1, "送入模型", "帧窗口", false, "124 帧 · 5.17 秒", "22", "226 帧 · 9.42 秒", "68"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
