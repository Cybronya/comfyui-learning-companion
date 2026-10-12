# LTXVSetAudioVideoMaskByTime

## 节点类型

`LTXVSetAudioVideoMaskByTime`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `av_latent:LATENT`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `model:MODEL`（1 次）
- `vae:VAE`（1 次）
- `audio_vae:VAE`（1 次）
- `spatial_mask:MASK`（1 次）
- `start_time:FLOAT`（1 次）
- `end_time:FLOAT`（1 次）
- `video_fps:FLOAT`（1 次）

## 输出

- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `av_latent:LATENT`（1 次）
- `video_latent_blend_coefficients:FLOAT`（1 次）
- `video_pixel_blend_coefficients:FLOAT`（1 次）
- `output_5:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 100, 24, true, false, 0, 0, 93]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
