# DZ_Face_Detailer

## 节点类型

`DZ_Face_Detailer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 10 个 workflow 中。

## 输入

- `model:MODEL`（10 次）
- `positive:CONDITIONING`（10 次）
- `negative:CONDITIONING`（10 次）
- `latent_image:LATENT`（10 次）
- `vae:VAE`（10 次）
- `seed:INT`（6 次）
- `steps:INT`（6 次）
- `cfg:FLOAT`（6 次）
- `sampler_name:COMBO`（6 次）
- `scheduler:COMBO`（6 次）

## 输出

- `LATENT:LATENT`（10 次）
- `MASK:MASK`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "fixed", 15, 2, "euler_ancestral", "sgm_uniform", 0.7000000000000001, 50, "face", "erode", 0, 100]`（2 次）
- `[649568003797710, "fixed", 10, 1, "euler_ancestral", "sgm_uniform", 0.4, 50, "face", "erode", 0, 100]`（1 次）
- `[852241236503654, "randomize", 10, 1, "euler_ancestral", "sgm_uniform", 0.6, 50, "face", "erode", 0, 100]`（1 次）
- `[196449754455599, "fixed", 30, 1, "euler_ancestral", "sgm_uniform", 1, 50, "face", "dilate", 40, 30]`（1 次）
- `[104140763621284, "randomize", 20, 1.5, "euler_ancestral", "sgm_uniform", 0.8, 5, "box", "dilate", 3, 3]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
