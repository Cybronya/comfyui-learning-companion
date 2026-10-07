# EsesImageEffectBloom

## 节点类型

`EsesImageEffectBloom`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `mask:MASK`（4 次）
- `low_threshold:FLOAT`（2 次）
- `high_threshold:FLOAT`（2 次）
- `blur_type:COMBO`（2 次）
- `blur_radius:FLOAT`（2 次）
- `highlights_brightness:FLOAT`（2 次）
- `blend_mode:COMBO`（2 次）
- `fade:FLOAT`（2 次）
- `blur_resolution_limit_px:INT`（2 次）

## 输出

- `modified_image:IMAGE`（4 次）
- `highlights_image:IMAGE`（4 次）
- `image:IMAGE`（4 次）
- `mask:MASK`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.7000000000000002, 0.95, "gaussian", 15, 1, "screen", 0.7000000000000002, 2048]`（1 次）
- `[0.7000000000000002, 0.95, "gaussian", 15, 1.0000000000000002, "screen", 0.7000000000000002, 2048]`（1 次）
- `[0.7000000000000002, 0.95, "gaussian", 15, 1.0000000000000002, "screen", 0.5000000000000001, 2048]`（1 次）
- `[0.10000000000000002, 0.9500000000000002, "gaussian", 15, 1.0000000000000002, "screen", 0.15000000000000002, 2048]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
