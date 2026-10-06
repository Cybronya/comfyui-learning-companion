# Yuan_H3ProgressiveSampler

## 节点类型

`Yuan_H3ProgressiveSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `vae:VAE`（2 次）
- `latent_image:LATENT`（2 次）
- `sampler:SAMPLER`（2 次）
- `sigmas:SIGMAS`（2 次）
- `seed:INT`（2 次）
- `transition_step:INT`（2 次）
- `lowres_scale:FLOAT`（2 次）
- `rho:FLOAT`（2 次）

## 输出

- `潜空间:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[305127315592435, "randomize", 6, 0.5, 0, 0.5, 1, "h3_upscaler_sharpness_2000steps_v0.1_fp32.safetensors", false, true, `（1 次）
- `[137195302914843, "randomize", 6, 0.5, 0, 0.5, 1, "h3_upscaler_sharpness_2000steps_v0.1_fp32.safetensors", false, true, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
