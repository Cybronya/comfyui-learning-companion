# HFEPostProcessor (lrzjason)

## 节点类型

`HFEPostProcessor (lrzjason)`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `latent_image:LATENT`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `noise_seed:INT`（1 次）
- `steps:INT`（1 次）
- `hfe_steps:INT`（1 次）
- `cfg:FLOAT`（1 次）
- `sampler_name:COMBO`（1 次）
- `scheduler:COMBO`（1 次）

## 输出

- `LATENT:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[160568321726404, "randomize", 8, 2, 1, "euler", "sgm_uniform", 1.05, 5, 0.05, 2, 0.5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
