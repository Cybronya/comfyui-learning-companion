# AudioSeparator

## 节点类型

`AudioSeparator`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:OPEN_UNMIX_MODEL`（1 次）
- `audio:AUDIO`（1 次）
- `video_frames:IMAGE`（1 次）

## 输出

- `audio:AUDIO`（1 次）
- `drums_audio:AUDIO`（1 次）
- `vocals_audio:AUDIO`（1 次）
- `bass_audio:AUDIO`（1 次）
- `other_audio:AUDIO`（1 次）
- `feature_pipe:FEATURE_PIPE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[30]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
