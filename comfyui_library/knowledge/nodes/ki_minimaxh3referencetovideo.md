# ki_MiniMaxH3ReferenceToVideo

## 节点类型

`ki_MiniMaxH3ReferenceToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）
- `vae:VAE`（2 次）
- `audio_vae:VAE`（2 次）
- `ref_images.ref_image_0:IMAGE`（2 次）
- `ref_images.ref_image_1:IMAGE`（2 次）
- `ref_images.ref_image_2:IMAGE`（2 次）
- `ref_videos.ref_video_0:IMAGE`（2 次）
- `ref_videos.ref_video_1:IMAGE`（2 次）
- `ref_video_audios.ref_video_audio_0:AUDIO`（2 次）
- `ref_audios.ref_audio_0:AUDIO`（2 次）

## 输出

- `positive:CONDITIONING`（2 次）
- `LATENT:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 1344, 768, 124, "2.0"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
