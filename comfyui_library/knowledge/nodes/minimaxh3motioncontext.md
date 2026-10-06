# MiniMaxH3MotionContext

## 节点类型

`MiniMaxH3MotionContext`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（2 次）
- `vae:VAE`（2 次）
- `latent:LATENT`（2 次）
- `context_frames:IMAGE`（2 次）
- `context_latent:LATENT`（2 次）
- `audio_vae:VAE`（2 次）
- `context_audio:AUDIO`（2 次）
- `context_length:COMBO`（2 次）
- `audio_context_length:INT`（2 次）

## 输出

- `conditioning:CONDITIONING`（2 次）
- `trim_frames:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["22", 24]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
