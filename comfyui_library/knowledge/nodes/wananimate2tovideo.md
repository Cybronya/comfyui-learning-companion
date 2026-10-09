# WanAnimate2ToVideo

## 节点类型

`WanAnimate2ToVideo`

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
- `reference_image:IMAGE`（2 次）
- `pose_video:IMAGE`（2 次）
- `clip_vision_output:CLIP_VISION_OUTPUT`（2 次）
- `positive_pose:CONDITIONING`（2 次）
- `clip_vision_output_pose:CLIP_VISION_OUTPUT`（2 次）
- `continue_motion:IMAGE`（2 次）
- `width:INT`（2 次）

## 输出

- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent:LATENT`（2 次）
- `trim_latent:INT`（2 次）
- `trim_image:INT`（2 次）
- `video_frame_offset:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 81, 1, 0, 1, 0, 1, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
