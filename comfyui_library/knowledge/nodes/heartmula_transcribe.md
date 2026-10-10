# HeartMuLa_Transcribe

## 节点类型

`HeartMuLa_Transcribe`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio_input:AUDIO`（1 次）
- `temperature_tuple:STRING`（1 次）
- `no_speech_threshold:FLOAT`（1 次）
- `logprob_threshold:FLOAT`（1 次）

## 输出

- `lyrics_text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["0.0,0.1,0.2,0.4", 0.4, -1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
