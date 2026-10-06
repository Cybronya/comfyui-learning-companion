# KSamplerCacheable

## 节点类型

`KSamplerCacheable`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `latent_image:LATENT`（3 次）
- `seed:INT`（3 次）
- `steps:INT`（3 次）
- `cfg:FLOAT`（3 次）
- `sampler_name:COMBO`（3 次）
- `scheduler:COMBO`（3 次）
- `denoise:FLOAT`（3 次）

## 输出

- `LATENT:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[612469955575595, "randomize", 50, 1, "euler", "simple", 1]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
