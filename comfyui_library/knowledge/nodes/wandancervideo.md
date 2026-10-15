# WanDancerVideo

## 节点类型

`WanDancerVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 12 个 workflow 中。

## 输入

- `positive:CONDITIONING`（24 次）
- `negative:CONDITIONING`（24 次）
- `vae:VAE`（24 次）
- `clip_vision_output:CLIP_VISION_OUTPUT`（24 次）
- `clip_vision_output_ref:CLIP_VISION_OUTPUT`（24 次）
- `start_image:IMAGE`（24 次）
- `mask:MASK`（24 次）
- `audio_encoder_output:AUDIO_ENCODER_OUTPUT`（24 次）
- `width:INT`（24 次）
- `height:INT`（24 次）

## 输出

- `positive:CONDITIONING`（24 次）
- `negative:CONDITIONING`（24 次）
- `latent:LATENT`（24 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[480, 832, 149]`（20 次）
- `[480, 544, 149]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
