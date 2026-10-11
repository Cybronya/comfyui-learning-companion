# PainterAudioCut

## 节点类型

`PainterAudioCut`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `audio:AUDIO`（3 次）
- `frame_rate:FLOAT`（3 次）
- `start_frame:INT`（3 次）
- `end_frame:INT`（3 次）
- `tail_silence_frames:INT`（3 次）

## 输出

- `trimmed_audio:AUDIO`（3 次）
- `aligned_frames:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[21.5, -4, 121, 22]`（2 次）
- `[30, -4, 30, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
