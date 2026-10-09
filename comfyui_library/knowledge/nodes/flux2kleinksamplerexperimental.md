# Flux2KleinKSamplerExperimental

## 节点类型

`Flux2KleinKSamplerExperimental`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `latent_image:LATENT`（1 次）
- `negative:CONDITIONING`（1 次）
- `steps:INT`（1 次）
- `seed:INT`（1 次）
- `denoise:FLOAT`（1 次）
- `base_shift:FLOAT`（1 次）
- `max_shift:FLOAT`（1 次）
- `cfg_scale:FLOAT`（1 次）

## 输出

- `LATENT:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4, 1, "fixed", 0.55, 0.5, 1.15, 1, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
