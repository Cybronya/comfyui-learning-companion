# workflow>k采样器

## 节点类型

`workflow>k采样器`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `VAE:VAE`（1 次）
- `VAEEncode pixels:IMAGE`（1 次）
- `VAEEncode vae:VAE`（1 次）
- `模型:MODEL`（1 次）
- `正面条件:CONDITIONING`（1 次）
- `负面条件:CONDITIONING`（1 次）
- `VAEDecode vae:VAE`（1 次）
- `降噪:FLOAT`（1 次）

## 输出

- `Latent:LATENT`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[640675500435529, "randomize", 25, 3, "ddim", "ddim_uniform", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
