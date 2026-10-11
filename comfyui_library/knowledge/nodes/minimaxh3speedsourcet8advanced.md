# MiniMaxH3SPEEDSourceT8Advanced

## 节点类型

`MiniMaxH3SPEEDSourceT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `video_vae:VAE`（1 次）
- `audio_vae:VAE`（1 次）
- `drive_audio:AUDIO`（1 次）
- `final_audio:AUDIO`（1 次）
- `first_frame:IMAGE`（1 次）
- `last_frame:IMAGE`（1 次）
- `ref_images.ref_image_0:IMAGE`（1 次）
- `ref_videos.ref_video_0:IMAGE`（1 次）
- `ref_video_audios.ref_video_audio_0:AUDIO`（1 次）

## 输出

- `speed_source:H3_T8_SPEED_SOURCE`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["integrated_multimodal_description: [Shot 1] A 15.00-second cinematic 3D animated martial-arts feature with polished st`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
