# WanDancerPadKeyframesList

## 节点类型

`WanDancerPadKeyframesList`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 12 个 workflow 中。

## 输入

- `images:IMAGE`（12 次）
- `audio:AUDIO`（12 次）
- `segment_length:INT`（12 次）
- `num_segments:INT`（12 次）

## 输出

- `keyframes_sequence:IMAGE`（12 次）
- `keyframes_mask:MASK`（12 次）
- `audio_segment:AUDIO`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[149, 1]`（7 次）
- `[149, 2]`（4 次）
- `[149, 5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
