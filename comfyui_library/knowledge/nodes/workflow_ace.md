# workflow>ace

## 节点类型

`workflow>ace`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `模型:MODEL`（1 次）
- `正面条件:CONDITIONING`（1 次）
- `负面条件:CONDITIONING`（1 次）
- `采样器:SAMPLER`（1 次）
- `Sigmas:SIGMAS`（1 次）
- `Latent:LATENT`（1 次）
- `KSampler model:MODEL`（1 次）
- `KSampler positive:CONDITIONING`（1 次）
- `KSampler negative:CONDITIONING`（1 次）
- `KSampler latent_image:LATENT`（1 次）

## 输出

- `降噪输出:LATENT`（1 次）
- `图像:IMAGE`（1 次）
- `VAEDecode 图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ae.sft", true, 1, 30, 1, 0, "sgm_uniform", 1, 965157568326189, "randomize", 306561146443373, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
