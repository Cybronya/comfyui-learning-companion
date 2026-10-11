# PainterAI2V

## 节点类型

`PainterAI2V`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_high_noise:MODEL`（2 次）
- `model_low_noise:MODEL`（2 次）
- `model_patch:MODEL_PATCH`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `vae:VAE`（2 次）
- `audio_encoder_output_1:AUDIO_ENCODER_OUTPUT`（2 次）
- `clip_vision_output:CLIP_VISION_OUTPUT`（2 次）
- `start_image:IMAGE`（2 次）
- `end_image:IMAGE`（2 次）

## 输出

- `high_model:MODEL`（2 次）
- `low_model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent:LATENT`（2 次）
- `trim_image:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 201, 20, 9, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
