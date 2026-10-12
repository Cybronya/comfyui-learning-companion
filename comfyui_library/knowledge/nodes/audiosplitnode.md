# AudioSplitNode

## 节点类型

`AudioSplitNode`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `audio:AUDIO`（2 次）
- `split_duration:FLOAT`（2 次）
- `min_silence_duration:FLOAT`（2 次）
- `silence_threshold:FLOAT`（2 次）
- `max_silence_search:FLOAT`（2 次）
- `noise_reduction:BOOLEAN`（2 次）
- `adaptive_threshold:BOOLEAN`（2 次）
- `spectral_analysis:BOOLEAN`（2 次）
- `high_precision:BOOLEAN`（2 次）

## 输出

- `audio_list:AUDIO_LIST`（2 次）
- `count:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[3, 0.15, 0.010000000000000002, 0.4000000000000001, true, true, true, true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
