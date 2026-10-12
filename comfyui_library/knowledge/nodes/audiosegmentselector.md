# AudioSegmentSelector

## 节点类型

`AudioSegmentSelector`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（2 次）
- `time_segments:STRING`（2 次）
- `index:INT`（2 次）

## 输出

- `audio_segment:AUDIO`（2 次）
- `start_sec:FLOAT`（2 次）
- `end_sec:FLOAT`（2 次）
- `duration:FLOAT`（2 次）
- `frame_num:INT`（2 次）
- `FPS_out:FLOAT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 0, 25, false, 12, -50]`（1 次）
- `["", 9, 25, false, 12, -50]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
