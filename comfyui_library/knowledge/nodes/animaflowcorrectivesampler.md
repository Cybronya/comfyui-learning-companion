# AnimaFlowCorrectiveSampler

## 节点类型

`AnimaFlowCorrectiveSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（4 次）
- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `latent_image:LATENT`（4 次）
- `flow_settings:ANIMA_FLOW_SETTINGS`（4 次）
- `vae:VAE`（4 次）
- `seed:INT`（4 次）
- `steps:INT`（4 次）
- `cfg:FLOAT`（4 次）
- `cfg_mode:COMBO`（4 次）

## 输出

- `latent:LATENT`（4 次）
- `image:IMAGE`（4 次）
- `log:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[214, "fixed", 1, 1.5, "ramp cfg", "flow_euler", "flow_diffusers_linear_shift", 3, 0.01, false]`（2 次）
- `[214, "fixed", 10, 1.5, "ramp cfg", "flow_euler", "flow_diffusers_linear_shift", 3, 0.05, false]`（1 次）
- `[214, "fixed", 10, 1.5, "ramp cfg", "flow_euler", "flow_diffusers_linear_shift", 3, 0.05000000000000001, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
