# MiniMaxH3AVDecodeT8GH

## 节点类型

`MiniMaxH3AVDecodeT8GH`

## 分类

Decoding

## 作用

解码类节点：把编码数据还原（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `av_latent:LATENT`（1 次）
- `video_vae:VAE`（1 次）
- `audio_vae:VAE`（1 次）

## 输出

- `frames:IMAGE`（1 次）
- `generated_audio:AUDIO`（1 次）
- `video_latent:LATENT`（1 次）
- `audio_latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
