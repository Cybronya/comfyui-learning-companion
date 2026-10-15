# WanSCAILMultirefInfinity

## 节点类型

`WanSCAILMultirefInfinity`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `model:MODEL`（4 次）
- `vae:VAE`（4 次）
- `pose_video:IMAGE`（4 次）
- `pose_video_mask:IMAGE`（4 次）
- `reference_image:IMAGE`（4 次）
- `reference_image_mask:IMAGE`（4 次）
- `clip_vision_output:CLIP_VISION_OUTPUT`（4 次）
- `width:INT`（4 次）

## 输出

- `images:IMAGE`（4 次）
- `latent:LATENT`（4 次）
- `total_frames:INT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 896, 688003211104317, "randomize", 6, 1, "euler", "simple", 1, 81, 5, 0, false, false, 1, 0, 1, false]`（1 次）
- `[512, 896, 1017109800830647, "randomize", 6, 1, "euler", "simple", 1, 81, 5, 0, false, false, 1, 0, 1, false]`（1 次）
- `[512, 896, 749137302998129, "randomize", 6, 1, "euler", "simple", 1, 81, 5, 0, false, false, 1, 0, 1, false]`（1 次）
- `[512, 896, 982664494486619, "randomize", 6, 1, "euler", "simple", 1, 81, 5, 0, false, false, 1, 0, 1, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
