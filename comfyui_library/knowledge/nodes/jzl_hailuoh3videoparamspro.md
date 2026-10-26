# JZL_HailuoH3VideoParamsPro

## 节点类型

`JZL_HailuoH3VideoParamsPro`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 12 个 workflow 中。

## 输入

- `aspect_ratio:COMBO`（12 次）
- `megapixels:FLOAT`（12 次）
- `multiple:INT`（12 次）
- `frames_display:STRING`（12 次）
- `duration:INT`（12 次）
- `scale_factor:FLOAT`（12 次）
- `upscale_scale:FLOAT`（12 次）

## 输出

- `Width:INT`（12 次）
- `Height:INT`（12 次）
- `Frames:INT`（12 次）
- `参考图放大系数:FLOAT`（12 次）
- `二采放大倍数:FLOAT`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["9:16 (Portrait Widescreen)", 0.5, 32, "544 × 960  |  估算帧数: 192", 8, 1.5, 2]`（9 次）
- `["16:9 (Widescreen)", 0.5, 32, "960 × 544  |  估算帧数: 243", 10, 1.5, 2]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
