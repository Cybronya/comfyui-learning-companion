# BitDanceSampler

## 节点类型

`BitDanceSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 15 个 workflow 中。

## 输入

- `model:BITDANCE_MODEL`（15 次）
- `vae:BITDANCE_VAE`（15 次）
- `positive:BITDANCE_TEXT_EMBEDS`（15 次）
- `negative:BITDANCE_TEXT_EMBEDS`（15 次）
- `resolution:BITDANCE_RESOLUTION`（15 次）
- `sampler_name:COMBO`（15 次）
- `num_sampling_steps:INT`（15 次）
- `guidance_scale:FLOAT`（15 次）
- `num_images:INT`（15 次）
- `seed:INT`（15 次）

## 输出

- `bitdance_latent:BITDANCE_LATENT`（15 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["euler_maruyama", 20, 7.5, 1, 75530124509923, "randomize"]`（1 次）
- `["euler_maruyama", 50, 7.5, 1, 688479063805719, "randomize"]`（1 次）
- `["euler_maruyama", 30, 7.5, 1, 26315894306513, "randomize"]`（1 次）
- `["euler_maruyama", 20, 7.5, 1, 440066402030866, "randomize"]`（1 次）
- `["euler_maruyama", 20, 7.5, 1, 891909938787338, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
