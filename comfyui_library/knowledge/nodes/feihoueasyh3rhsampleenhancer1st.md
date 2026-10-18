# FeiHouEasyH3RHSampleEnhancer1st

## 节点类型

`FeiHouEasyH3RHSampleEnhancer1st`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `h3_context:MINIMAX_H3_CONTEXT`（1 次）
- `sampler_name:COMBO`（1 次）
- `scheduler:COMBO`（1 次）
- `total_steps:INT`（1 次）
- `first_steps:INT`（1 次）
- `cfg:FLOAT`（1 次）
- `negative_prompt:STRING`（1 次）
- `semantic_bridge_on:BOOLEAN`（1 次）
- `semantic_bridge:COMBO`（1 次）

## 输出

- `guider:GUIDER`（1 次）
- `sampler:SAMPLER`（1 次）
- `sigmas:SIGMAS`（1 次）
- `latent:LATENT`（1 次）
- `h3_context:MINIMAX_H3_CONTEXT`（1 次）
- `video_vae:VAE`（1 次）
- `audio_vae:VAE`（1 次）
- `fps:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["dual_clock_euler", "simple", 9, 4, 1, "", true, "MiniMaxH3_SemanticBridge_v1.safetensors", 0.1, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
