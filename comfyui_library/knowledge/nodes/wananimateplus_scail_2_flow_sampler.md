# WanAnimatePlus SCAIL_2 Flow Sampler

## 节点类型

`WanAnimatePlus SCAIL_2 Flow Sampler`

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
- `latent:LATENT`（1 次）
- `vae:VAE`（1 次）
- `steps:INT`（1 次）
- `cfg:FLOAT`（1 次）
- `sampler_name:COMBO`（1 次）
- `scheduler:COMBO`（1 次）
- `shift:FLOAT`（1 次）

## 输出

- `samples:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[6, 1, "dpmpp_sde", "simple", 5, 803786878875861, "randomize", true, 0.5, 1, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
