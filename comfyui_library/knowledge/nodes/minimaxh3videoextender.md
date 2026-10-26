# MiniMaxH3VideoExtender

## 节点类型

`MiniMaxH3VideoExtender`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（5 次）
- `latent:LATENT`（5 次）
- `vae:VAE`（5 次）
- `prev_frames:IMAGE`（5 次）
- `prev_latent:LATENT`（5 次）
- `prev_audio:AUDIO`（5 次）
- `audio_vae:VAE`（5 次）
- `mode:COMBO`（5 次）
- `context_length:INT`（5 次）
- `encode_mode:COMBO`（5 次）

## 输出

- `conditioning:CONDITIONING`（5 次）
- `trim_frames:INT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto", 22, "video", "head", "disabled", 22, "timeline"]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
