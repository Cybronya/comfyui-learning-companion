# MergeAudioNode

## 节点类型

`MergeAudioNode`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio1:*`（1 次）
- `audio2:*`（1 次）
- `audio3:*`（1 次）
- `audio4:*`（1 次）
- `merge_algorithm:COMBO`（1 次）
- `sample_rate:COMBO`（1 次）
- `normalize:BOOLEAN`（1 次）
- `crossfade_duration:FLOAT`（1 次）
- `volume_balance:FLOAT`（1 次）
- `vocal_pitch_shift:FLOAT`（1 次）

## 输出

- `merged_audio:AUDIO`（1 次）
- `merge_info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["mean", "auto", true, 0.1, 0.5000000000000001, 0, 0, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
