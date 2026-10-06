# SUPIR_Upscale

## 节点类型

`SUPIR_Upscale`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `captions:STRING`（2 次）
- `supir_model:COMBO`（1 次）
- `sdxl_ckpt:COMBO`（1 次）
- `seed:INT`（1 次）
- `resize_method:COMBO`（1 次）
- `scale_by:FLOAT`（1 次）
- `steps:INT`（1 次）
- `restoration_scale:FLOAT`（1 次）
- `cfg_scale:FLOAT`（1 次）

## 输出

- `upscaled_image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["SUPIR-v0F.ckpt", null, 1008324804478597, "randomize", "lanczos", 2, 45, -1, 4, "high quality, detailed", "bad quality,`（1 次）
- `["SUPIR-v0F.ckpt", "Juggernaut-XL-v9.safetensors", 64541813743588, "randomize", "lanczos", 1.5000000000000002, 45, -1, 4`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
