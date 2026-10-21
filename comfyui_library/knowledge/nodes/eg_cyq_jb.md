# EG_CYQ_JB

## 节点类型

`EG_CYQ_JB`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `image:IMAGE`（1 次）
- `vae:VAE`（1 次）
- `mask:MASK`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `seed:INT`（1 次）
- `steps:INT`（1 次）
- `cfg:FLOAT`（1 次）
- `sampler_name:COMBO`（1 次）

## 输出

- `LATENT:LATENT`（1 次）
- `结果图像:IMAGE`（1 次）
- `采样图:IMAGE`（1 次）
- `采样遮罩:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[852553184671596, "randomize", 20, 8, "euler", "simple", 0.35, "原图", 6, true, 512, 50, 5, "2🐕出品，必出精品"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
