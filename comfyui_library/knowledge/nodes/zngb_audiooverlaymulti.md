# ZNGB_AudioOverlayMulti

## 节点类型

`ZNGB_AudioOverlayMulti`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `SourceVideo:VIDEO`（4 次）
- `audio_1:AUDIO`（4 次）
- `audio_2:AUDIO`（4 次）
- `inputcount:INT`（4 次）
- `source_start:FLOAT`（4 次）
- `source_end:FLOAT`（4 次）
- `sample_rate:INT`（4 次）
- `audio_1_start:FLOAT`（4 次）
- `audio_1_volume:FLOAT`（4 次）
- `audio_2_start:FLOAT`（4 次）

## 输出

- `audio:AUDIO`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[3, 0, 0, 44100, 0, 1, 0, 1, null]`（2 次）
- `[4, 0, 0, 44100, 0, 1, 0, 1, null]`（1 次）
- `[2, 0, 0, 44100, 0, 1, 0, 1, null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
