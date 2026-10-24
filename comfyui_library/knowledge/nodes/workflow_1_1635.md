# workflow>自定义采样器(高级)1

## 节点类型

`workflow>自定义采样器(高级)1`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `模型:MODEL`（2 次）
- `BasicGuider model:MODEL`（2 次）
- `CLIP:CLIP`（1 次）
- `Latent:LATENT`（1 次）
- `text:STRING`（1 次）
- `采样器:SAMPLER`（1 次）
- `条件:CONDITIONING`（1 次）
- `VAE:VAE`（1 次）
- `宽度:INT`（1 次）
- `高度:INT`（1 次）

## 输出

- `降噪输出:LATENT`（2 次）
- `采样器:SAMPLER`（1 次）
- `噪波生成:NOISE`（1 次）
- `条件:CONDITIONING`（1 次）
- `输出:LATENT`（1 次）
- `引导:GUIDER`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["euler", 801133146365630, "fixed", 3.5, "simple", 20, 0.25, "", [false, true]]`（1 次）
- `[715148694686616, "randomize", 1, "beta", 30, 1, 512, 512]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
