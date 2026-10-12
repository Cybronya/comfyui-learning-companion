# WanFourFrameReferenceUltimate

## 节点类型

`WanFourFrameReferenceUltimate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `positive:CONDITIONING`（5 次）
- `negative:CONDITIONING`（5 次）
- `vae:VAE`（5 次）
- `frame_1_image:IMAGE`（5 次）
- `frame_2_image:IMAGE`（5 次）
- `frame_3_image:IMAGE`（5 次）
- `frame_4_image:IMAGE`（5 次）
- `clip_vision_frame_1:CLIP_VISION_OUTPUT`（5 次）
- `clip_vision_frame_2:CLIP_VISION_OUTPUT`（5 次）
- `clip_vision_frame_3:CLIP_VISION_OUTPUT`（5 次）

## 输出

- `negative:CONDITIONING`（5 次）
- `latent:LATENT`（5 次）
- `positive_high_noise:CONDITIONING`（4 次）
- `positive_low_noise:CONDITIONING`（4 次）
- `positive_high:CONDITIONING`（1 次）
- `positive_low:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[480, 832, 121, 1, 0.5, 0.33, 0.4, "enable", 0.67, 0.4, "enable", 16, 16]`（1 次）
- `[576, 1024, 241, 1, "SINGLE_PERSON", 0.33, 0.53, 0, "enable", 0.67, 0.42, 0, "enable"]`（1 次）
- `[1024, 576, 81, 1, "SINGLE_PERSON", 0.33, 0.53, 0, "enable", 0.67, 0.42, 0, "enable"]`（1 次）
- `[720, 720, 81, 1, "SINGLE_PERSON", 0.33, 0.53, 0, "enable", 0.67, 0.42, 0, "enable"]`（1 次）
- `[480, 832, 121, 1, 0.5, 0.33, 0.4, "enable", 0.67, 0.4, "enable", 16, "enable", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
