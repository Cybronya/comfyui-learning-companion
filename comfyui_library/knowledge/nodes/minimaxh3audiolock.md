# MiniMaxH3AudioLock

## 节点类型

`MiniMaxH3AudioLock`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `av_latent:LATENT`（1 次）
- `audio:AUDIO`（1 次）
- `audio_vae:VAE`（1 次）
- `mode:COMBO`（1 次）
- `strength:FLOAT`（1 次）

## 输出

- `av_latent:LATENT`（1 次）
- `audio:AUDIO`（1 次）
- `report:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["lock", 0.35]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
