# ElevenLabsSpeechToText

## 节点类型

`ElevenLabsSpeechToText`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）

## 输出

- `text:STRING`（1 次）
- `language_code:STRING`（1 次）
- `words_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["scribe_v2", false, false, 0.22, 0, "word", "", 0, 519926995, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
