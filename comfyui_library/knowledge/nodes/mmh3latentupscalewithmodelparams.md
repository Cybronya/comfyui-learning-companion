# MMH3LatentUpscaleWithModelParams

## 节点类型

`MMH3LatentUpscaleWithModelParams`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_name:COMBO`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `device:COMBO`（1 次）
- `precision:COMBO`（1 次）

## 输出

- `latent_upscale_param:H3_UPSCALE_PARAM`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["h3_upscaler_lms_v0.1_fp32.safetensors", 1280, 704, "cuda", "fp32"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
