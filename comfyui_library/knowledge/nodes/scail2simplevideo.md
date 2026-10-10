# SCAIL2SimpleVideo

## 节点类型

`SCAIL2SimpleVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `vae:VAE`（1 次）
- `sampler:SAMPLER`（1 次）
- `sigmas:SIGMAS`（1 次）
- `reference_image:IMAGE,SCAIL2_REFERENCE_PACK`（1 次）
- `pose_video:IMAGE`（1 次）
- `clip_vision:CLIP_VISION`（1 次）
- `driving_track_data:SAM3_TRACK_DATA`（1 次）

## 输出

- `frames:IMAGE`（1 次）
- `summary:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[801894018638053, "randomize", 1, "replacement", true, "chunk", 0, 81, 5, false, 81, 20]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
