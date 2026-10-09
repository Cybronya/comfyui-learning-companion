# WanFirstMiddleLastFrameToVideo

## 节点类型

`WanFirstMiddleLastFrameToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `vae:VAE`（1 次）
- `start_image:IMAGE`（1 次）
- `middle_image:IMAGE`（1 次）
- `end_image:IMAGE`（1 次）
- `clip_vision_start_image:CLIP_VISION_OUTPUT`（1 次）
- `clip_vision_middle_image:CLIP_VISION_OUTPUT`（1 次）
- `clip_vision_end_image:CLIP_VISION_OUTPUT`（1 次）
- `width:INT`（1 次）

## 输出

- `positive_high_noise:CONDITIONING`（1 次）
- `positive_low_noise:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1280, 720, 121, 1, "SINGLE_PERSON", 0.5000000000000001, 0.4900000000000001, 1, 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
