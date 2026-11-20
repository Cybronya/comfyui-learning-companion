# HYPIRUpscale

## 节点类型

`HYPIRUpscale`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:HYPIR_MODEL`（1 次）
- `image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `upscale_factor:INT`（1 次）
- `model_t:INT`（1 次）
- `coeff_t:INT`（1 次）
- `cfg_scale:FLOAT`（1 次）
- `denoise_strength:FLOAT`（1 次）
- `scheduler_type:COMBO`（1 次）
- `patch_size:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["high quality portrait, detailed face, sharp features", 2, 200, 100, 1, 1, "DDPM", 512, 256, 642687169412223, "randomiz`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
