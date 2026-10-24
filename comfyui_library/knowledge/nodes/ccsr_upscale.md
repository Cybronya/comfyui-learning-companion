# CCSR_Upscale

## 节点类型

`CCSR_Upscale`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `ccsr_model:CCSRMODEL`（4 次）
- `image:IMAGE`（4 次）
- `resize_method:COMBO`（4 次）
- `scale_by:FLOAT`（4 次）
- `steps:INT`（4 次）
- `t_max:FLOAT`（4 次）
- `t_min:FLOAT`（4 次）
- `sampling_method:COMBO`（4 次）
- `tile_size:INT`（4 次）
- `tile_stride:INT`（4 次）

## 输出

- `upscaled_image:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["nearest-exact", 1.5000000000000002, 45, 0.6667, 0.3333, "ccsr_tiled_mixdiff", 512, 256, 1024, 1024, "wavelet", false, `（1 次）
- `["lanczos", 2.0000000000000004, 45, 0.6667, 0.3333, "ccsr_tiled_mixdiff", 512, 256, 1024, 1024, "adain", false, 54490208`（1 次）
- `["nearest-exact", 1.5000000000000002, 45, 0.6667, 0.3333, "ccsr_tiled_mixdiff", 512, 256, 1024, 1024, "wavelet", false, `（1 次）
- `["nearest-exact", 1.5, 45, 0.6667, 0.3333, "ccsr", 512, 256, 1024, 1024, "wavelet", false, 381138128745286, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
