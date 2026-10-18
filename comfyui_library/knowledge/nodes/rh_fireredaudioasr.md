# RH_FireRedAudioASR

## 节点类型

`RH_FireRedAudioASR`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 13 个 workflow 中。

## 输入

- `model:FIREREDAUDIO_MODEL`（13 次）
- `audio:AUDIO`（13 次）
- `generate_timestamps:BOOLEAN`（12 次）
- `timestamp_segment_seconds:INT`（12 次）
- `max_new_tokens:INT`（12 次）

## 输出

- `text:STRING`（13 次）
- `timestamp_text:STRING`（13 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 30, 300]`（12 次）
- `[false, 30, 300]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
