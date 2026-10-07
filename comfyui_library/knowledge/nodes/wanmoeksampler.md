# WanMoeKSampler

## 节点类型

`WanMoeKSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_high_noise:MODEL`（1 次）
- `model_low_noise:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent_image:LATENT`（1 次）
- `boundary:FLOAT`（1 次）
- `seed:INT`（1 次）
- `steps:INT`（1 次）
- `cfg_high_noise:FLOAT`（1 次）
- `cfg_low_noise:FLOAT`（1 次）

## 输出

- `LATENT:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.875, 911623611783310, "randomize", 4, 1, 1, "euler_ancestral", "beta", 8.000000000000002, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
