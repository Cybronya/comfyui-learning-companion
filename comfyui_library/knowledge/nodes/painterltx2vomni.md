# PainterLTX2Vomni

## 节点类型

`PainterLTX2Vomni`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `video_vae:VAE`（3 次）
- `audio_vae:VAE`（3 次）
- `start_image:IMAGE`（3 次）
- `end_image:IMAGE`（3 次）
- `source_video:IMAGE`（3 次）
- `reference_image1:IMAGE`（3 次）
- `reference_image2:IMAGE`（3 次）
- `width:INT`（3 次）

## 输出

- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `video_latent:LATENT`（3 次）
- `audio_latent:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[864, 1536, 241, 30, 1, 0, 0]`（2 次）
- `[768, 512, 97, 30.000000000000007, 1.0000000000000002, 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
