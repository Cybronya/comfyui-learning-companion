# H3AudioRefineSampler

## 节点类型

`H3AudioRefineSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `model:MODEL`（5 次）
- `positive:CONDITIONING`（5 次）
- `negative:CONDITIONING`（5 次）
- `latent:LATENT`（5 次）
- `seed:INT`（5 次）
- `steps:INT`（5 次）
- `cfg:FLOAT`（5 次）
- `sampler_name:COMBO`（5 次）
- `scheduler:COMBO`（5 次）
- `audio_denoise:FLOAT`（5 次）

## 输出

- `LATENT:LATENT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "fixed", 6, 1, "euler", "beta", 0.3, 0]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
