# Krea2ControlImageEncode

## 节点类型

`Krea2ControlImageEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `control_image:IMAGE`（7 次）
- `vae:VAE`（7 次）
- `latent:LATENT`（7 次）
- `resize:COMBO`（7 次）
- `upscale_method:COMBO`（7 次）
- `crop:COMBO`（7 次）
- `channel_mode:COMBO`（7 次）
- `normalize:COMBO`（7 次）
- `invert:BOOLEAN`（7 次）
- `batch_mode:COMBO`（7 次）

## 输出

- `control_latent:LATENT`（7 次）
- `encoded_control_image:IMAGE`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["match_latent_size", "bilinear", "center", "rgb", "none", false, "independent_images"]`（6 次）
- `["match_latent_size", "lanczos", "center", "rgb", "none", false, "independent_images"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
