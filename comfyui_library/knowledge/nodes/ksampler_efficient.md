# KSampler (Efficient)

## 节点类型

`KSampler (Efficient)`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent_image:LATENT`（2 次）
- `optional_vae:VAE`（2 次）
- `script:SCRIPT`（2 次）
- `seed:INT`（2 次）
- `steps:INT`（2 次）
- `cfg:FLOAT`（2 次）
- `sampler_name:COMBO`（2 次）

## 输出

- `MODEL:MODEL`（2 次）
- `CONDITIONING+:CONDITIONING`（2 次）
- `CONDITIONING-:CONDITIONING`（2 次）
- `LATENT:LATENT`（2 次）
- `VAE:VAE`（2 次）
- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[403214011463433, null, 25, 1, "euler", "simple", 1, "auto", "true"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
