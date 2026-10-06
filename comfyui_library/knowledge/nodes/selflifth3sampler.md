# SelfLiftH3Sampler

## 节点类型

`SelfLiftH3Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `model:MODEL`（8 次）
- `positive:CONDITIONING`（8 次）
- `negative:CONDITIONING`（8 次）
- `vae:VAE`（8 次）
- `latent_image:LATENT`（8 次）
- `sampler:SAMPLER`（8 次）
- `sigmas:SIGMAS`（8 次）
- `model_hires:MODEL`（8 次）
- `seed:INT`（8 次）
- `cfg:FLOAT`（8 次）

## 输出

- `LATENT:LATENT`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "fixed", 1, 6, 0.5, 0, 0.5, 1, "h3_upscaler_lms_v0.1.safetensors", false, true]`（5 次）
- `[161265879125788, "randomize", 1, 5, 0.5000000000000001, 0, 0.5, 1, "minimax_h3_latent_upscaler_3d_fp16_V2.safetensors",`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
