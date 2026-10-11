# BerniniS2VConditioning

## 节点类型

`BerniniS2VConditioning`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `vae:VAE`（2 次）
- `audio_encoder_output:AUDIO_ENCODER_OUTPUT`（2 次）
- `source_video:IMAGE`（2 次）
- `reference_video:IMAGE`（2 次）
- `reference_image_0:IMAGE`（2 次）
- `reference_image_1:IMAGE`（2 次）
- `reference_image_2:IMAGE`（2 次）
- `reference_image_3:IMAGE`（2 次）

## 输出

- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 576, 81, 1, 1024]`（1 次）
- `[832, 480, 81, 1, 1024]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
