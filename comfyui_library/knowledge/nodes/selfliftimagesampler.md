# SelfLiftImageSampler

## 节点类型

`SelfLiftImageSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `vae:VAE`（1 次）
- `latent_image:LATENT`（1 次）
- `sampler:SAMPLER`（1 次）
- `sigmas:SIGMAS`（1 次）
- `seed:INT`（1 次）
- `cfg:FLOAT`（1 次）
- `transition_step:INT`（1 次）

## 输出

- `LATENT:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[883864430983446, "randomize", 1, 6, 0.5, 0.3, 0.5, 1, "nearest"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
