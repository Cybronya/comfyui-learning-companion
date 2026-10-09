# LTXDirector

## 节点类型

`LTXDirector`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `audio_vae:VAE`（1 次）
- `optional_latent:LATENT`（1 次）
- `global_prompt:STRING`（1 次）
- `frame_rate:FLOAT`（1 次）
- `custom_width:INT`（1 次）
- `custom_height:INT`（1 次）
- `resize_method:COMBO`（1 次）
- `start_second:FLOAT`（1 次）

## 输出

- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `video_latent:LATENT`（1 次）
- `audio_latent:LATENT`（1 次）
- `guide_data:GUIDE_DATA`（1 次）
- `motion_guide_data:MOTION_GUIDE_DATA`（1 次）
- `frame_rate:FLOAT`（1 次）
- `combined_audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 3, 4, 0, 72, 96, "{\"mainTrackEnabled\":true,\"audioTrackEnabled\":true,\"motionTrackEnabled\":false,\"propHeight\":`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
