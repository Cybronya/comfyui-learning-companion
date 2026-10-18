# GenerateNoise

## 节点类型

`GenerateNoise`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `sigmas:SIGMAS`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `batch_size:INT`（1 次）
- `seed:INT`（1 次）
- `multiplier:FLOAT`（1 次）
- `constant_batch_noise:BOOLEAN`（1 次）
- `normalize:BOOLEAN`（1 次）
- `latent_channels:COMBO`（1 次）

## 输出

- `LATENT:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, 1, 0, "fixed", 1, false, false, "16", "BCHW"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
