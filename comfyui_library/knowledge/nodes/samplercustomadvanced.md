# SamplerCustomAdvanced

## 节点类型

`SamplerCustomAdvanced`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 58 个 workflow 中。

## 输入

- `noise:NOISE`（83 次）
- `guider:GUIDER`（83 次）
- `sampler:SAMPLER`（83 次）
- `sigmas:SIGMAS`（83 次）
- `latent_image:LATENT`（83 次）

## 输出

- `output:LATENT`（83 次）
- `denoised_output:LATENT`（83 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[]`（79 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
