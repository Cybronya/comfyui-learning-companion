# WanSoundImageToVideo

## 节点类型

`WanSoundImageToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `vae:VAE`（2 次）
- `audio_encoder_output:AUDIO_ENCODER_OUTPUT`（2 次）
- `ref_image:IMAGE`（2 次）
- `control_video:IMAGE`（2 次）
- `ref_motion:IMAGE`（2 次）
- `length:INT`（2 次）

## 输出

- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[640, 640, 77, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
