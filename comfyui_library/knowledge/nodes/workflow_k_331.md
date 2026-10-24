# workflow/k采样

## 节点类型

`workflow/k采样`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `VAE:VAE`（1 次）
- `模型:MODEL`（1 次）
- `正面条件:CONDITIONING`（1 次）
- `Latent:LATENT`（1 次）
- `CLIP:CLIP`（1 次）
- `CONDITIONING:CONDITIONING`（1 次）
- `MODEL:MODEL`（1 次）
- `Reroute VAE:VAE`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `CONDITIONING:CONDITIONING`（1 次）
- `Reroute CONDITIONING:CONDITIONING`（1 次）
- `MODEL:MODEL`（1 次）
- `VAEDecode 图像:IMAGE`（1 次）
- `VAE:VAE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["enable", 543894580517317, "randomize", 30, 1, "euler", "simple", 0, 10, "disable", "", "enable", 697249321551053, "ran`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
