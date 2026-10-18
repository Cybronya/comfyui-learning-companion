# FeiHouEasyH3RHSampleEnhancer2nd

## 节点类型

`FeiHouEasyH3RHSampleEnhancer2nd`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `h3_context:MINIMAX_H3_CONTEXT`（1 次）
- `1st_latent:LATENT`（1 次）
- `model:MODEL`（1 次）
- `wait_1st_video:*`（1 次）
- `latent_upscaler:COMBO`（1 次）
- `upscale_by:FLOAT`（1 次）
- `second_steps:INT`（1 次）
- `default_trigger_words:BOOLEAN`（1 次）

## 输出

- `guider:GUIDER`（1 次）
- `sampler:SAMPLER`（1 次）
- `sigmas:SIGMAS`（1 次）
- `latent:LATENT`（1 次）
- `h3_context:MINIMAX_H3_CONTEXT`（1 次）
- `video_vae:VAE`（1 次）
- `audio_vae:VAE`（1 次）
- `fps:FLOAT`（1 次）
- `audio_1:AUDIO`（1 次）
- `duration_control:FEIHOU_H3_DURATION_CONTROL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["h3_upscaler_lms_v0.1.safetensors", 1.5, 5, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
