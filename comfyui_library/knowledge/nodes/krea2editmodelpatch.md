# Krea2EditModelPatch

## 节点类型

`Krea2EditModelPatch`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `source_latent:LATENT`（2 次）
- `source_latent_b:LATENT`（2 次）
- `ref_boost_mask:MASK`（2 次）
- `vae:VAE`（2 次）
- `source_image:IMAGE`（2 次）
- `source_image_b:IMAGE`（2 次）
- `target_latent:LATENT`（2 次）
- `ref_boost:FLOAT`（2 次）
- `ref_boost_a:FLOAT`（2 次）

## 输出

- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4, 1, "fit"]`（1 次）
- `[1, 1, "fit"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
