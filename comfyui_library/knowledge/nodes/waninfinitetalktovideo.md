# WanInfiniteTalkToVideo

## 节点类型

`WanInfiniteTalkToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `mode.audio_encoder_output_2:AUDIO_ENCODER_OUTPUT`（20 次）
- `mode.mask_1:MASK`（20 次）
- `mode.mask_2:MASK`（20 次）
- `model:MODEL`（4 次）
- `model_patch:MODEL_PATCH`（4 次）
- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `vae:VAE`（4 次）
- `audio_encoder_output_1:AUDIO_ENCODER_OUTPUT`（4 次）
- `clip_vision_output:CLIP_VISION_OUTPUT`（4 次）

## 输出

- `model:MODEL`（4 次）
- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `latent:LATENT`（4 次）
- `trim_image:INT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["two_speakers", 832, 480, 81, 9, 1]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
