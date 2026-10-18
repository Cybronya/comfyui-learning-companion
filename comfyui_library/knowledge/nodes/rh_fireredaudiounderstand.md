# RH_FireRedAudioUnderstand

## 节点类型

`RH_FireRedAudioUnderstand`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `model:FIREREDAUDIO_MODEL`（7 次）
- `audio:AUDIO`（7 次）
- `prompt:STRING`（7 次）
- `audio_2:AUDIO`（6 次）
- `enable_thinking:BOOLEAN`（6 次）
- `max_new_tokens:INT`（6 次）

## 输出

- `answer:STRING`（7 次）
- `reasoning:STRING`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", true, 1024]`（4 次）
- `["女人想和男人干什么", true, 1024]`（1 次）
- `[false, 1024]`（1 次）
- `["false", 1024, 1024]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
