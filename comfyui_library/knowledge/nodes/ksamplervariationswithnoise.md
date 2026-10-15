# KSamplerVariationsWithNoise+

## 节点类型

`KSamplerVariationsWithNoise+`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `latent_image:LATENT`（2 次）
- `main_seed:INT:seed`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `variation_seed:INT:seed`（2 次）
- `steps:INT`（2 次）
- `cfg:FLOAT`（2 次）
- `sampler_name:COMBO`（2 次）
- `scheduler:COMBO`（2 次）

## 输出

- `LATENT:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[20, 8, "euler", "simple", 0.17, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
