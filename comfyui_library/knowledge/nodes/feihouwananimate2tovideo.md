# FeiHouWanAnimate2ToVideo

## 节点类型

`FeiHouWanAnimate2ToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `vae:VAE`（3 次）
- `reference_image:IMAGE`（3 次）
- `pose_video:IMAGE`（3 次）
- `clip_vision_output:CLIP_VISION_OUTPUT`（3 次）
- `positive_pose:CONDITIONING`（3 次）
- `clip_vision_output_pose:CLIP_VISION_OUTPUT`（3 次）
- `continue_motion:IMAGE`（3 次）

## 输出

- `model:MODEL`（3 次）
- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `latent:LATENT`（3 次）
- `trim_latent:INT`（3 次）
- `trim_image:INT`（3 次）
- `video_frame_offset:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 81, 81, 1, 0, 1, 0, 1, 1]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
