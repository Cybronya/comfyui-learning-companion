# SZ_KleinTiledKSampler

## 节点类型

`SZ_KleinTiledKSampler`

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
- `latent_blend:LATENT`（1 次）
- `seed:INT`（1 次）
- `steps:INT`（1 次）
- `cfg:FLOAT`（1 次）
- `sampler_name:COMBO`（1 次）
- `scheduler:COMBO`（1 次）

## 输出

- `latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[900966197316183, "fixed", 4, 1, "sa_solver", "FlowMatchEulerDiscreteScheduler", 1, 384, 384, 96, 0.30000000000000004, 0`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
