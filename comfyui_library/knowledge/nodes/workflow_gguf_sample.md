# workflow>gguf-sample

## 节点类型

`workflow>gguf-sample`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `noise:NOISE`（1 次）
- `guider:GUIDER`（1 次）
- `latent_image:LATENT`（1 次）

## 输出

- `SAMPLER:SAMPLER`（1 次）
- `SIGMAS:SIGMAS`（1 次）
- `output:LATENT`（1 次）
- `denoised_output:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["dpmpp_2m", "karras", 30, 0.7500000000000001]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
