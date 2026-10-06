# SeedVR2VideoUpscaler

## 节点类型

`SeedVR2VideoUpscaler`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 67 个 workflow 中。

## 输入

- `image:IMAGE`（71 次）
- `dit:SEEDVR2_DIT`（71 次）
- `vae:SEEDVR2_VAE`（71 次）
- `seed:INT`（71 次）
- `resolution:INT`（71 次）
- `max_resolution:INT`（71 次）
- `batch_size:INT`（71 次）
- `uniform_batch_size:BOOLEAN`（71 次）
- `color_correction:COMBO`（71 次）
- `temporal_overlap:INT`（71 次）

## 输出

- `image:IMAGE`（71 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[42, "fixed", 3840, 0, 1, false, "lab", 0, 0, 0, 0, "none", false]`（6 次）
- `[369, "fixed", 1024, 0, 1, false, "wavelet", 0, 0, 0, 0, "cpu", false]`（6 次）
- `[2461588580, "fixed", 1080, 0, 1, false, "lab", 0, 0, 0, 0, "cpu", false]`（6 次）
- `[666, "fixed", 1080, 0, 1, false, "lab", 0, 0, 0, 0, "cpu", false]`（5 次）
- `[1688711203, "increment", 2160, 4500, 1, false, "lab", 0, 0, 0, 0, "cpu", false]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
