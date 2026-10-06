# VOSR2Upscale

## 节点类型

`VOSR2Upscale`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 15 个 workflow 中。

## 输入

- `model:VOSR2_MODEL`（23 次）
- `image:IMAGE`（23 次）
- `upscale:INT`（23 次）
- `seed:INT`（23 次）
- `color_alignment:COMBO`（23 次）
- `tile_size:INT`（23 次）
- `tile_overlap:INT`（23 次）
- `vae_tile_size:INT`（23 次）
- `vae_tile_overlap:INT`（23 次）

## 输出

- `IMAGE:IMAGE`（23 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, 42, "fixed", "wavelet", 512, 64, 512, 64]`（8 次）
- `[4, 42, "fixed", "wavelet", 512, 64, 512, 64]`（5 次）
- `[4, 195027237476190, "randomize", "wavelet", 512, 64, 512, 64]`（4 次）
- `[4, 201333950591369, "randomize", "wavelet", 512, 64, 512, 64]`（2 次）
- `[2, 409176844146685, "randomize", "wavelet", 512, 64, 1024, 128]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
