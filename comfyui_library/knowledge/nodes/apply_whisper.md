# Apply Whisper

## 节点类型

`Apply Whisper`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `audio:AUDIO`（2 次）
- `model:COMBO`（2 次）
- `language:COMBO`（2 次）
- `prompt:STRING`（2 次）

## 输出

- `text:STRING`（2 次）
- `segments_alignment:whisper_alignment`（2 次）
- `words_alignment:whisper_alignment`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Belle-whisper-large-v3-zh-punct-ct2-float32", "auto", ""]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
