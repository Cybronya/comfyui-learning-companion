# H3KitSelfLiftSampler

## 节点类型

`H3KitSelfLiftSampler`

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
- `latent_image:LATENT`（1 次）
- `previous_latent:LATENT`（1 次）
- `sigmas:SIGMAS`（1 次）
- `context_vae:VAE`（1 次）
- `previous_frames:IMAGE`（1 次）
- `seed:INT`（1 次）
- `steps:INT`（1 次）

## 输出

- `sampled_latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1080026292710978, "randomize", 6, 1, "euler", "beta", 1, 2, 0.4000000000000001, "minimax_h3_latent_upscaler_3d_bf16.saf`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
