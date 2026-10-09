# easy minimaxH3AudioLock

## 节点类型

`easy minimaxH3AudioLock`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `latent:LATENT`（2 次）
- `audio_vae:VAE`（2 次）
- `audio:AUDIO`（2 次）
- `remix_strength:FLOAT`（2 次）
- `short_audio_mode:COMBO`（2 次）
- `prepend_frames:INT`（2 次）
- `frame_rate:FLOAT`（2 次）

## 输出

- `latent:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "silence", 0, 24]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
