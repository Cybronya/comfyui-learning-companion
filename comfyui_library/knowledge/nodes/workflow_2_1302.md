# workflow>彩样2

## 节点类型

`workflow>彩样2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `图像:IMAGE`（2 次）
- `VAE:VAE`（2 次）
- `GetImageSize image:IMAGE`（2 次）
- `条件:CONDITIONING`（2 次）
- `conditioning:CONDITIONING`（2 次）
- `模型:MODEL`（2 次）
- `sampler_name:COMBO`（2 次）
- `noise_seed:INT`（2 次）
- `batch_size:INT`（2 次）
- `steps:INT`（2 次）

## 输出

- `batch_size:INT`（2 次）
- `输出:LATENT`（2 次）
- `降噪输出:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["euler", 832041285273727, "randomize", 1, 6, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
