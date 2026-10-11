# WanVideoAddAudioEmbeds

## 节点类型

`WanVideoAddAudioEmbeds`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `embeds:WANVIDIMAGE_EMBEDS`（1 次）
- `audio_encoder_output:AUDIO_ENCODER_OUTPUT`（1 次）
- `ref_latent:LATENT`（1 次）
- `pose_latent:LATENT`（1 次）
- `frames:INT`（1 次）
- `audio_scale:FLOAT`（1 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[81, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
