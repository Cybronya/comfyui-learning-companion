# MiniMaxH3Unified

## 节点类型

`MiniMaxH3Unified`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）
- `vae:VAE`（2 次）
- `audio_vae:VAE`（2 次）
- `mode:COMFY_DYNAMICCOMBO_V3`（2 次）
- `mode.ref_image_size:COMBO`（2 次）
- `mode.ref_images.ref_image_0:IMAGE`（2 次）
- `mode.ref_videos.ref_video_0:IMAGE`（2 次）
- `mode.ref_video_audios.ref_video_audio_0:AUDIO`（2 次）
- `mode.ref_audios.ref_audio_0:AUDIO`（2 次）
- `prompt:STRING`（2 次）

## 输出

- `positive:CONDITIONING`（2 次）
- `av_latent:LATENT`（2 次）
- `audio:AUDIO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["omni_reference", "max", "", 1344, 768, 10, false, "{\"_ui\":{\"video_count\":0,\"audio_count\":0,\"image_count\":6},\"`（1 次）
- `["omni_reference", "max", "", 1344, 768, 10, false, "{\"_ui\":{\"video_count\":0,\"audio_count\":0,\"image_count\":4},\"`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
