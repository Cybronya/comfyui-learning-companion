# ClownsharkChainsampler_Beta

## 节点类型

`ClownsharkChainsampler_Beta`

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
- `sigmas:SIGMAS`（1 次）
- `latent_image:LATENT`（1 次）
- `guides:GUIDES`（1 次）
- `options:OPTIONS`（1 次）
- `eta:FLOAT`（1 次）
- `sampler_name:COMBO`（1 次）
- `steps_to_run:INT`（1 次）

## 输出

- `output:LATENT`（1 次）
- `denoised:LATENT`（1 次）
- `options:OPTIONS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.5, "exponential/res_2s", -1, 1, "resample", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
