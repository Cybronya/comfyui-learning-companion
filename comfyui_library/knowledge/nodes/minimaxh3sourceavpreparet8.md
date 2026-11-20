# MiniMaxH3SourceAVPrepareT8

## 节点类型

`MiniMaxH3SourceAVPrepareT8`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `video_latent:LATENT`（2 次）
- `audio_latent:LATENT`（2 次）
- `video_mode:COMBO`（2 次）
- `video_denoise_strength:FLOAT`（2 次）
- `audio_mode:COMBO`（2 次）
- `audio_denoise_strength:FLOAT`（2 次）
- `audio_fit_policy:COMBO`（2 次）
- `dtype_device_policy:COMBO`（2 次）

## 输出

- `av_latent:LATENT`（2 次）
- `video_latent:LATENT`（2 次）
- `audio_latent:LATENT`（2 次）
- `report:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["regenerate", 1, "lock", 0, "trim_to_video", "match_video"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
