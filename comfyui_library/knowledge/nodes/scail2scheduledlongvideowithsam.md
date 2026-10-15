# SCAIL2ScheduledLongVideoWithSAM

## 节点类型

`SCAIL2ScheduledLongVideoWithSAM`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 23 个 workflow 中。

## 输入

- `model:MODEL`（32 次）
- `clip:CLIP`（32 次）
- `vae:VAE`（32 次）
- `sampler:SAMPLER`（32 次）
- `sigmas:SIGMAS`（32 次）
- `clip_vision:CLIP_VISION`（32 次）
- `pose_video:IMAGE`（32 次）
- `sam_model:MODEL`（32 次）
- `sam_conditioning:CONDITIONING`（32 次）
- `reference_1:IMAGE`（32 次）

## 输出

- `frames:IMAGE`（32 次）
- `used_pose_video_mask:IMAGE`（32 次）
- `used_reference_mask_timeline:IMAGE`（32 次）
- `summary:STRING`（32 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["# frames | reference | prompt | negative | boundary_overlap\n49 | 1 | first segment prompt | |\n121 | 2 | second segme`（12 次）
- `["# frames | reference | prompt | negative | boundary_overlap\n49 | 1 | first segment prompt | |\n121 | 2 | second segme`（4 次）
- `["# frames | reference | prompt | negative | boundary_overlap\n49 | 1 | first segment prompt | |\n121 | 2 | second segme`（2 次）
- `["# frames | reference | prompt | negative | boundary_overlap\n49 | 1 | first segment prompt | |\n121 | 2 | second segme`（2 次）
- `["# frames | reference | prompt | negative | boundary_overlap\n49 | 1 | first segment prompt | |\n121 | 2 | second segme`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
