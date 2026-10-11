# GoohaiMinimaxH3LatentUpscalerGH

## 节点类型

`GoohaiMinimaxH3LatentUpscalerGH`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 11 个 workflow 中。

## 输入

- `av_latent:LATENT`（11 次）
- `model_name:COMBO`（11 次）
- `mode:COMFY_DYNAMICCOMBO_V3`（11 次）
- `mode.scale:FLOAT`（11 次）
- `align:INT`（11 次）
- `force_unload:BOOLEAN`（11 次）
- `device:COMBO`（11 次）
- `precision:COMBO`（11 次）

## 输出

- `av_latent:LATENT`（11 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["minimax_h3_latent_upscaler_3d_fp16.safetensors", "scale by multiplier", 2, 32, false, "cuda", "fp16"]`（11 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
