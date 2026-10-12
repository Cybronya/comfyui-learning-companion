# LTXVExtendSampler

## 节点类型

`LTXVExtendSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `model:MODEL`（5 次）
- `vae:VAE`（5 次）
- `latents:LATENT`（5 次）
- `guider:GUIDER`（5 次）
- `sampler:SAMPLER`（5 次）
- `sigmas:SIGMAS`（5 次）
- `noise:NOISE`（5 次）
- `num_new_frames:INT`（1 次）

## 输出

- `denoised_output:LATENT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[80, 24]`（3 次）
- `[48, 24]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
