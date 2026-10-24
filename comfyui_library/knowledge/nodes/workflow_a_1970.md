# workflow>傲雪A

## 节点类型

`workflow>傲雪A`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（5 次）
- `LayerUtility: ImageScaleByAspectRatio V2 image:IMAGE`（5 次）
- `遮罩:MASK`（5 次）
- `text1:STRING`（5 次）
- `text2:STRING`（5 次）
- `upscale_method:COMBO`（5 次）
- `scale_by:FLOAT`（5 次）
- `model_name:COMBO`（5 次）
- `clip_name1:COMBO`（5 次）
- `clip_name2:COMBO`（5 次）

## 输出

- `图像:IMAGE`（5 次）
- `遮罩:MASK`（5 次）
- `原始大小:BOX`（5 次）
- `width:INT`（5 次）
- `height:INT`（5 次）
- `显示帮助:STRING`（5 次）
- `降噪输出:LATENT`（5 次）
- `RECONSTRUCTED_IMAGE:IMAGE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["nearest-exact", 2, "4x-UltraSharp.pth", "t5xxl_fp8_e4m3fn.safetensors", "clip_l.safetensors", "flux", "default", "high`（1 次）
- `["nearest-exact", 2, "4x-UltraSharp.pth", "t5xxl_fp8_e4m3fn.safetensors", "clip_l.safetensors", "flux", "default", "high`（1 次）
- `["nearest-exact", 2, "4x-UltraSharp.pth", "t5xxl_fp8_e4m3fn.safetensors", "clip_l.safetensors", "flux", "default", "high`（1 次）
- `["nearest-exact", 2, "4x-UltraSharp.pth", "t5xxl_fp8_e4m3fn.safetensors", "clip_l.safetensors", "flux", "default", "high`（1 次）
- `["nearest-exact", 2, "4x-UltraSharp.pth", "t5xxl_fp8_e4m3fn.safetensors", "clip_l.safetensors", "flux", "default", "high`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
