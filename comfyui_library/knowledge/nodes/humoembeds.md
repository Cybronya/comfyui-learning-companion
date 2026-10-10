# HuMoEmbeds

## 节点类型

`HuMoEmbeds`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `whisper_model:WHISPERMODEL`（3 次）
- `vae:WANVAE`（3 次）
- `reference_images:IMAGE`（3 次）
- `audio:AUDIO`（3 次）
- `num_frames:INT`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `audio_scale:FLOAT`（3 次）
- `audio_cfg_scale:FLOAT`（3 次）
- `audio_start_percent:FLOAT`（3 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[65, 1, 2.5, 1, 2.5, 0, 1, false]`（2 次）
- `[65, 1, 2.5, 1, 1.0500000000000003, 0, 1, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
