# MochiWrapperSamplerCustom

## 节点类型

`MochiWrapperSamplerCustom`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MOCHIMODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `sigmas:SIGMAS`（2 次）
- `latents:LATENT`（2 次）
- `sampler:SAMPLER`（2 次）

## 输出

- `samples:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4.5, 0, "fixed", false]`（1 次）
- `[1, 1, "fixed", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
