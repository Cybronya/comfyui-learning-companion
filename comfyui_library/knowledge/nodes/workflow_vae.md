# workflow>vae解码编码

## 节点类型

`workflow>vae解码编码`

## 分类

Latent

## 作用

VAE 相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `VAE:VAE`（1 次）
- `Latent:LATENT`（1 次）
- `VAEDecode vae:VAE`（1 次）
- `VAEDecode samples:LATENT`（1 次）
- `VAEDecode 2 vae:VAE`（1 次）
- `VAEEncode pixels:IMAGE`（1 次）
- `VAEEncode vae:VAE`（1 次）
- `VAEDecode 2 samples:LATENT`（1 次）
- `VAEDecode 3 vae:VAE`（1 次）

## 输出

- `Latent:LATENT`（1 次）
- `图像:IMAGE`（1 次）
- `VAEDecode 图像:IMAGE`（1 次）
- `VAEEncode Latent:LATENT`（1 次）
- `VAEDecode 4 图像:IMAGE`（1 次）
- `VAEDecode 5 图像:IMAGE`（1 次）
- `VAEDecode 6 图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
