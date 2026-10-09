# IterativeImageUpscale

## 节点类型

`IterativeImageUpscale`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `pixels:IMAGE`（6 次）
- `upscaler:UPSCALER`（6 次）
- `vae:VAE`（6 次）
- `upscale_factor:FLOAT`（6 次）
- `steps:INT`（6 次）
- `temp_prefix:STRING`（6 次）
- `step_mode:COMBO`（6 次）
- `vae_compression:INT`（6 次）

## 输出

- `image:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, 1, "", "simple", 8]`（3 次）
- `[1.5, 1, "", "simple", 8]`（1 次）
- `[["128", 0], ["167", 0], "", "simple", 8]`（1 次）
- `[4, 2, "", "simple", 8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
