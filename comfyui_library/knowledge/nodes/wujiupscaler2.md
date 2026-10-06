# WujiUpscaler2

## 节点类型

`WujiUpscaler2`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `upscale:INT`（3 次）
- `preview:BOOLEAN`（3 次）
- `dlss5:COMBO`（3 次）
- `dlss5_mode:COMBO`（3 次）

## 输出

- `图像:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4, false, "仅 VOSR2", "图像"]`（2 次）
- `[2, false, "SeedVR2 + DLSS", "图像"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
