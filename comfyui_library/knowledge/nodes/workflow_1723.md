# workflow/自定义采样器(高级)

## 节点类型

`workflow/自定义采样器(高级)`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `模型:MODEL`（1 次）
- `BasicGuider model:MODEL`（1 次）
- `条件:CONDITIONING`（1 次）
- `VAE:VAE`（1 次）
- `放大模型:UPSCALE_MODEL`（1 次）

## 输出

- `宽度:INT`（1 次）
- `高度:INT`（1 次）
- `降噪输出:LATENT`（1 次）
- `图像:IMAGE`（1 次）
- `ImageUpscaleWithModel 图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[106394572012813, "randomize", "euler", "832x1152 (0.72)", 1, 0, 0, "simple", 20, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
