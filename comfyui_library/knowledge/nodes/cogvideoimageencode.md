# CogVideoImageEncode

## 节点类型

`CogVideoImageEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `vae:VAE`（3 次）
- `start_image:IMAGE`（3 次）
- `end_image:IMAGE`（3 次）
- `enable_tiling:BOOLEAN`（3 次）
- `noise_aug_strength:FLOAT`（3 次）
- `strength:FLOAT`（3 次）
- `start_percent:FLOAT`（3 次）
- `end_percent:FLOAT`（3 次）

## 输出

- `samples:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, 0, 1, 0, 1]`（2 次）
- `[false, 0.056, 1, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
