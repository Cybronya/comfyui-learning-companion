# MinimaxH3LatentUpscaler3D

## 节点类型

`MinimaxH3LatentUpscaler3D`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `latent:*`（4 次）
- `model_name:COMBO`（4 次）
- `mode:COMFY_DYNAMICCOMBO_V3`（4 次）
- `mode.scale:FLOAT`（4 次）
- `align:INT`（4 次）
- `device:COMBO`（4 次）
- `precision:COMBO`（4 次）
- `enable_chunking:BOOLEAN`（4 次）

## 输出

- `latent:*`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["minimax_h3_latent_upscaler_3d_fp16.safetensors", "scale by multiplier", 1.5000000000000002, 32, "cuda", "fp16", false]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
