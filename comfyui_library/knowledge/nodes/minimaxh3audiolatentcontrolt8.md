# MiniMaxH3AudioLatentControlT8

## 节点类型

`MiniMaxH3AudioLatentControlT8`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `av_latent:LATENT`（2 次）
- `source_audio:AUDIO`（2 次）
- `audio_vae:VAE`（2 次）
- `mode:COMBO`（2 次）
- `strength:FLOAT`（2 次）

## 输出

- `av_latent:LATENT`（2 次）
- `source_audio:AUDIO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["lock", 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
