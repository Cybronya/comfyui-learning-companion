# workflow/采样器

## 节点类型

`workflow/采样器`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `VAE:VAE`（3 次）
- `CLIP:CLIP`（2 次）
- `文本:STRING`（2 次）
- `模型:MODEL`（2 次）
- `BasicGuider model:MODEL`（2 次）
- `model:MODEL`（1 次）
- `图像:IMAGE`（1 次）
- `VAEDecode vae:VAE`（1 次）
- `条件:CONDITIONING`（1 次）

## 输出

- `降噪输出:LATENT`（3 次）
- `图像:IMAGE`（3 次）
- `宽度:INT`（1 次）
- `高度:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ipndm", 768, 1280, 298108675271667, "randomize", 10, 1.15, 0.5, 3.5, "simple", 30, 1, ""]`（1 次）
- `["euler", 483809468834270, "randomize", "simple", 28, 1, 3.5, ""]`（1 次）
- `[760882299175430, "randomize", "euler", "832x1152 (0.72)", 1, 0, 0, "simple", 30, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
