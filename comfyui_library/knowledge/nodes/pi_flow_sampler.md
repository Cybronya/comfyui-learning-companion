# pi-Flow Sampler

## 节点类型

`pi-Flow Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `conditioning:CONDITIONING`（1 次）
- `latent_image:LATENT`（1 次）
- `seed:INT`（1 次）
- `steps:INT`（1 次）
- `substeps:INT`（1 次）
- `final_step_size_scale:FLOAT`（1 次）
- `diffusion_coefficient:FLOAT`（1 次）
- `gm_temperature:COMBO`（1 次）
- `manual_gm_temperature:FLOAT`（1 次）

## 输出

- `LATENT:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[246395911187349, "randomize", 4, 128, 0.5000000000000001, 0, "auto", 1, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
