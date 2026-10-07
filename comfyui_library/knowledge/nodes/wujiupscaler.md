# WujiUpscaler

## 节点类型

`WujiUpscaler`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `放大模型:COMBO`（1 次）
- `最短边尺寸:INT`（1 次）
- `颜色校对:COMBO`（1 次）
- `预览开关:BOOLEAN`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["seedvr2_ema_3b-Q4_K_M.gguf", 1080, "lab", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
