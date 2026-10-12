# VideoGlitchArtTransitionNode

## 节点类型

`VideoGlitchArtTransitionNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video1:IMAGE`（1 次）
- `video2:IMAGE`（1 次）
- `glitch_style:COMBO`（1 次）
- `total_frames:INT`（1 次）
- `fps:INT`（1 次）
- `glitch_intensity:FLOAT`（1 次）
- `corruption_rate:FLOAT`（1 次）
- `scanline_frequency:FLOAT`（1 次）
- `noise_amount:FLOAT`（1 次）
- `digital_artifacts:BOOLEAN`（1 次）

## 输出

- `video:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["signal_interference", 36, 24, 1, 0.3, 5, 0.2, true, true, true, true, 6, "#000000", 640, 640, 90]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
