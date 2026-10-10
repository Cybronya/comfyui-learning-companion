# WanVacePhantomSimpleV2

## 节点类型

`WanVacePhantomSimpleV2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `vae:VAE`（1 次）
- `latent_in:LATENT`（1 次）
- `control_video:IMAGE`（1 次）
- `control_masks:MASK`（1 次）
- `vace_reference:IMAGE`（1 次）
- `phantom_images:IMAGE`（1 次）
- `width:INT`（1 次）

## 输出

- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `neg_phant_img:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）
- `trim_latent:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 81, 1, 0.8, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
