# LTXVModelConfigurator

## 节点类型

`LTXVModelConfigurator`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `vae:VAE`（3 次）
- `conditioning:IMAGE`（3 次）
- `initial_latent:LATENT`（3 次）
- `frames_number:INT`（2 次）
- `frame_rate:INT`（2 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `model:MODEL`（3 次）
- `latent:LATENT`（3 次）
- `sigma_shift:FLOAT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Custom", 768, 512, 105, 25, 1, true, 29]`（2 次）
- `["Custom", 768, 512, 65, 25, 1, true, 29]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
