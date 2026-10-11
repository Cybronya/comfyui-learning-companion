# AudioInfo

## 节点类型

`AudioInfo`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `audio:AUDIO`（2 次）
- `frame_rate:FLOAT`（2 次）

## 输出

- `total_frames:INT`（2 次）
- `frames_per_beat:INT`（2 次）
- `frames_per_bar:INT`（2 次）
- `frames_per_quarter:INT`（2 次）
- `frames_per_eighth:INT`（2 次）
- `audio_duration:FLOAT`（2 次）
- `beats_per_second:FLOAT`（2 次）
- `detected_bpm:FLOAT`（2 次）
- `detected_bpm_rounded:INT`（2 次）
- `sample_rate:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[30]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
