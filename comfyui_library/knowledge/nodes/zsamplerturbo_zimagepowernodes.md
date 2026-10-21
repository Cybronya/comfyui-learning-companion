# ZSamplerTurbo //ZImagePowerNodes

## 节点类型

`ZSamplerTurbo //ZImagePowerNodes`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `latent_input:LATENT`（1 次）
- `seed:INT`（1 次）
- `steps:INT`（1 次）
- `denoise:FLOAT`（1 次）

## 输出

- `latent_output:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[581310093469444, "randomize", 9, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
