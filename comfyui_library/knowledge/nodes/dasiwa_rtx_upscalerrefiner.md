# DaSiWa_RTX_UpscalerRefiner

## 节点类型

`DaSiWa_RTX_UpscalerRefiner`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `images:IMAGE`（3 次）
- `denoise:BOOLEAN`（3 次）
- `denoise_quality:COMBO`（3 次）
- `deblur:BOOLEAN`（3 次）
- `deblur_quality:COMBO`（3 次）
- `upscale:COMBO`（3 次）
- `upscale_quality:COMBO`（3 次）
- `resize_type:COMBO`（3 次）
- `scale:FLOAT`（3 次）
- `megapixels:FLOAT`（3 次）

## 输出

- `images:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, "Ultra", false, "Ultra", "VSR", "Ultra", "Scale", 2, 2, 1920, 1080, "8", "16:9", "Center Crop (Fill)", 0, false,`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
