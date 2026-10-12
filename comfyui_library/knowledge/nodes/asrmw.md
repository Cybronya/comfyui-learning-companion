# ASRMW

## 节点类型

`ASRMW`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 10 个 workflow 中。

## 输入

- `音频:AUDIO`（11 次）
- `模型:COMBO`（11 次）
- `每句最大长度:INT`（11 次）
- `卸载模型:BOOLEAN`（11 次）
- `seed:INT`（11 次）

## 输出

- `纯文本:STRING`（11 次）
- `时间戳单词:STRING`（11 次）
- `时间戳句子:STRING`（11 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Belle-whisper-large-v3-zh-punct-ct2", 1000, true, 874334492652031, "randomize"]`（1 次）
- `["Belle-whisper-large-v3-zh-punct-ct2-float32", 1000, true, 1040993761473031, "randomize"]`（1 次）
- `["Belle-whisper-large-v3-zh-punct-ct2", 1000, true, 1083698269399507, "randomize"]`（1 次）
- `["Belle-whisper-large-v3-zh-punct-ct2", 1000, true, 770615937402153, "randomize"]`（1 次）
- `["faster-whisper-large-v3-turbo-ct2", 10, true, 21029485093061, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
