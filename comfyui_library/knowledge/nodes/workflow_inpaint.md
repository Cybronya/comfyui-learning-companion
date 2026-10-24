# workflow/inpaint

## 节点类型

`workflow/inpaint`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `model:MODEL`（1 次）
- `conditioning:CONDITIONING`（1 次）
- `noise:NOISE`（1 次）
- `sampler:SAMPLER`（1 次）
- `sigmas:SIGMAS`（1 次）
- `latent_image:LATENT`（1 次）
- `vae:VAE`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `denoised_output:LATENT`（1 次）
- `VAEDecode IMAGE:IMAGE`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
