# KSampler SDXL (Eff.)

## 节点类型

`KSampler SDXL (Eff.)`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `sdxl_tuple:SDXL_TUPLE`（1 次）
- `latent_image:LATENT`（1 次）
- `optional_vae:VAE`（1 次）
- `script:SCRIPT`（1 次）
- `noise_seed:INT`（1 次）

## 输出

- `SDXL_TUPLE:SDXL_TUPLE`（1 次）
- `LATENT:LATENT`（1 次）
- `VAE:VAE`（1 次）
- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[387175924970679, null, 25, 5.5, "heun", "beta", 18, 22, "auto", "true", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
