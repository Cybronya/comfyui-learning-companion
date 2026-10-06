# SelfLiftAvatarH3Sampler

## 节点类型

`SelfLiftAvatarH3Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 27 个 workflow 中。

## 输入

- `model:MODEL`（36 次）
- `positive:CONDITIONING`（36 次）
- `negative:CONDITIONING`（36 次）
- `vae:VAE`（36 次）
- `latent_image:LATENT`（36 次）
- `sampler:SAMPLER`（36 次）
- `sigmas:SIGMAS`（36 次）
- `model_hires:MODEL`（36 次）
- `seed:INT`（36 次）
- `cfg:FLOAT`（36 次）

## 输出

- `LATENT:LATENT`（36 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[999, "fixed", 1, 6, 0.5, 0, 0.5, 1, "h3_upscaler_sharpness_2000steps_v0.1_fp32.safetensors", false]`（9 次）
- `[599913279995092, "randomize", 1, 5, 0.4, 0, 0.5, 1, "minimax_h3_latent_upscaler_3d_bf16.safetensors", false]`（3 次）
- `[266964588646822, "randomize", 1, 5, 0.5, 0, 0.5, 1, "minimax_h3_latent_upscaler_3d_fp16.safetensors", false]`（3 次）
- `[999, "fixed", 1, 6, 0.5, 0, 0.5, 1, "h3_upscaler_lms_v0.1_fp32.safetensors", false]`（2 次）
- `[999, "fixed", 1, 5, 0.5, 0, 0.5, 1, "minimax_h3_latent_upscaler_3d_fp16.safetensors", false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
