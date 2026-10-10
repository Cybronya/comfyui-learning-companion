# LTXVLoopingSampler

## 节点类型

`LTXVLoopingSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `vae:VAE`（1 次）
- `noise:NOISE`（1 次）
- `sampler:SAMPLER`（1 次）
- `sigmas:SIGMAS`（1 次）
- `guider:GUIDER`（1 次）
- `latents:LATENT`（1 次）
- `optional_cond_images:IMAGE`（1 次）
- `optional_guiding_latents:LATENT`（1 次）
- `optional_positive_conditionings:CONDITIONING`（1 次）

## 输出

- `denoised_output:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[56, 24, 1, 0.5, 1, 1, 1, 1, 0, 0, 1000, "0"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
