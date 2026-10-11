# ComfyEverAnimate

## 节点类型

`ComfyEverAnimate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `vae:VAE`（4 次）
- `clip_vision_output:CLIP_VISION_OUTPUT`（4 次）
- `reference_image:IMAGE`（4 次）
- `face_video:IMAGE`（4 次）
- `pose_video:IMAGE`（4 次）
- `background_video:IMAGE`（4 次）
- `character_mask:MASK`（4 次）
- `continue_motion:IMAGE`（4 次）

## 输出

- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `latent:LATENT`（4 次）
- `trim_latent:INT`（4 次）
- `trim_image:INT`（4 次）
- `video_frame_offset:INT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 81, 1, 4, 1, 0, 1, 1, 1, 1]`（2 次）
- `[832, 480, 81, 1, 4, 1, 0, 1, 1, 1, 5]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
