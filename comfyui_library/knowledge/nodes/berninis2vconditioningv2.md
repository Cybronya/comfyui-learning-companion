# BerniniS2VConditioningV2

## 节点类型

`BerniniS2VConditioningV2`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `vae:VAE`（1 次）
- `audio_1:AUDIO_ENCODER_OUTPUT`（1 次）
- `mask_1:MASK`（1 次）
- `audio_2:AUDIO_ENCODER_OUTPUT`（1 次）
- `mask_2:MASK`（1 次）
- `source_video:IMAGE`（1 次）
- `reference_video:IMAGE`（1 次）
- `reference_image_0:IMAGE`（1 次）

## 输出

- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 81, 1, -1, 4, 1, 848]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
