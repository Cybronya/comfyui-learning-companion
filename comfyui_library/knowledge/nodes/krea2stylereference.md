# Krea2StyleReference

## 节点类型

`Krea2StyleReference`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `vae:VAE`（2 次）
- `target_latent:LATENT`（2 次）
- `reference_image:IMAGE`（2 次）
- `fit:COMBO`（2 次）
- `upscale_method:COMBO`（2 次）

## 输出

- `reference_latent:LATENT`（2 次）
- `reference_preview:IMAGE`（2 次）
- `debug:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["crop", "lanczos"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
