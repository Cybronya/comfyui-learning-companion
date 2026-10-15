# WanSCAILInfinity

## 节点类型

`WanSCAILInfinity`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `positive:CONDITIONING`（5 次）
- `negative:CONDITIONING`（5 次）
- `model:MODEL`（5 次）
- `vae:VAE`（5 次）
- `pose_video:IMAGE`（5 次）
- `pose_video_mask:IMAGE`（5 次）
- `reference_image:IMAGE`（5 次）
- `reference_image_mask:IMAGE`（5 次）
- `clip_vision_output:CLIP_VISION_OUTPUT`（5 次）
- `width:INT`（5 次）

## 输出

- `images:IMAGE`（5 次）
- `latent:LATENT`（5 次）
- `total_frames:INT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 896, 123, "fixed", 6, 1, "euler", "simple", 1, 81, 5, 0, false, false, 1, 0, 1, false]`（2 次）
- `[512, 896, 1, "fixed", 6, 1, "euler", "simple", 1, 121, 5, 0, false, true, 1, 0, 1, false]`（1 次）
- `[512, 896, 1, "fixed", 6, 1, "euler", "simple", 1, 121, 5, 0, false, true, 1, 0, 1, true]`（1 次）
- `[512, 896, 274394539301386, "randomize", 6, 1, "euler", "simple", 1, 81, 5, 0, false, false, 1, 0, 1, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
