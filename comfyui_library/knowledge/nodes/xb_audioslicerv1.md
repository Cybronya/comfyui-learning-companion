# XB_AudioSlicerV1

## 节点类型

`XB_AudioSlicerV1`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:COMBO`（1 次）
- `fps:FLOAT`（1 次）
- `start_time:FLOAT`（1 次）
- `end_time:FLOAT`（1 次）
- `duration_display:STRING`（1 次）

## 输出

- `audio:AUDIO`（1 次）
- `frame_count:INT`（1 次）
- `fps:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["8eb48abeb64e99a1ac414ac8e3bb3d55afb16ecb316f21e2f224f6afd2ae2e49.mp3", 24, 35.00000000000001, 35.04166666666667, "1 帧 `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
