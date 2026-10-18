# T8MuLaCoverAudioCondition

## 节点类型

`T8MuLaCoverAudioCondition`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MULACOVER_MODEL`（2 次）
- `audio:AUDIO`（2 次）
- `bpm:FLOAT`（2 次）
- `semitone_shift:INT`（2 次）
- `octave_shift:INT`（2 次）

## 输出

- `condition:MULACOVER_CONDITION`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
