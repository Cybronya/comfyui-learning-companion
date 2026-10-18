# H3AutoContextSampler

## 节点类型

`H3AutoContextSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `vae:VAE`（1 次）
- `audio_vae:VAE`（1 次）
- `clip:CLIP`（1 次）
- `parameter:DICT`（1 次）
- `sampler:SAMPLER`（1 次）
- `sigmas:SIGMAS`（1 次）
- `latent_input:LATENT`（1 次）
- `info:DICT`（1 次）
- `first_frame:IMAGE`（1 次）

## 输出

- `latent:LATENT`（1 次）
- `denoised_latent:LATENT`（1 次）
- `info:DICT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 73, "fixed", 8, 1, "euler", "simple", 1, true, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
