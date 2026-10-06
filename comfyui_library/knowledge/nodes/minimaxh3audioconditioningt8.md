# MiniMaxH3AudioConditioningT8

## 节点类型

`MiniMaxH3AudioConditioningT8`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 28 个 workflow 中。

## 输入

- `clip:CLIP`（43 次）
- `video_vae:VAE`（43 次）
- `audio_vae:VAE`（43 次）
- `drive_audio:AUDIO`（43 次）
- `final_audio:AUDIO`（43 次）
- `first_frame:IMAGE`（43 次）
- `last_frame:IMAGE`（43 次）
- `ref_images.ref_image_0:IMAGE`（43 次）
- `ref_images.ref_image_1:IMAGE`（43 次）
- `ref_videos.ref_video_0:IMAGE`（43 次）

## 输出

- `positive:CONDITIONING`（43 次）
- `av_latent:LATENT`（43 次）
- `mux_audio:AUDIO`（43 次）
- `conditioned_prompt:STRING`（43 次）
- `media_map_json:STRING`（43 次）
- `report:STRING`（43 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["A woman in red Hanfu spins rapidly through the night sky, flowing silk and synchronized wind ambience, cinematic light`（7 次）
- `["A woman in red Hanfu spins rapidly through the night sky, flowing silk and synchronized wind ambience, cinematic light`（7 次）
- `["", 1344, 768, 124, "Ref2VA — 参考生音视频", "remix_source", 0, false, 1, true, "max", "official_2_to_15s", false]`（6 次）
- `["A woman in red Hanfu spins rapidly through the night sky, flowing silk and synchronized wind ambience, cinematic light`（3 次）
- `["A woman in red Hanfu spins rapidly through the night sky, flowing silk and synchronized wind ambience, cinematic light`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
