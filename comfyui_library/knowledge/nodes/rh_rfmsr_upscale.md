# RH_RFMSR_Upscale

## 节点类型

`RH_RFMSR_Upscale`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `rfmsr_model:RH_RFMSR_MODEL`（1 次）
- `image:IMAGE`（1 次）
- `scale:FLOAT`（1 次）
- `steps:INT`（1 次）
- `flow_sigma:FLOAT`（1 次）
- `seed:INT`（1 次）
- `color_correction:COMBO`（1 次）
- `tile_mode:COMBO`（1 次）
- `tile_size:INT`（1 次）
- `tile_stride:INT`（1 次）

## 输出

- `Upscaled Image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, 15, 1.0000000000000002, 642108338969835, "randomize", "wavelet", "auto", 512, 256]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
