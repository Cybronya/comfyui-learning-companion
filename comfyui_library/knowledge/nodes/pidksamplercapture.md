# PiDKSamplerCapture

## 节点类型

`PiDKSamplerCapture`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 12 个 workflow 中。

## 输入

- `model:MODEL`（12 次）
- `positive:CONDITIONING`（12 次）
- `negative:CONDITIONING`（12 次）
- `latent_image:LATENT`（12 次）
- `seed:INT`（12 次）
- `steps:INT`（12 次）
- `cfg:FLOAT`（12 次）
- `sampler_name:COMBO`（12 次）
- `scheduler:COMBO`（12 次）
- `denoise:FLOAT`（12 次）

## 输出

- `final_latent:LATENT`（12 次）
- `pid_latent:LATENT`（12 次）
- `pid_sigma:FLOAT`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[191166039668422, "fixed", 9, 1, "euler", "beta", 1, 8]`（3 次）
- `[191166039668422, "fixed", 28, 1, "euler", "simple", 1, 26]`（1 次）
- `[191166039668422, "fixed", 50, 4, "euler", "FlowMatchEulerDiscreteScheduler", 1, 46]`（1 次）
- `[15137491282269, "randomize", 4, 1, "euler", "beta", 1, 4]`（1 次）
- `[161426513335228, "randomize", 10, 1, "euler", "beta", 1, 9]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
