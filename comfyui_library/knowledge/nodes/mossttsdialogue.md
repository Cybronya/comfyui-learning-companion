# MossTTSDialogue

## 节点类型

`MossTTSDialogue`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `moss_pipe:MOSS_TTS_PIPE`（1 次）
- `s1_reference_audio:AUDIO`（1 次）
- `s2_reference_audio:AUDIO`（1 次）
- `language:COMBO`（1 次）
- `dialogue_text:STRING`（1 次）
- `speaker_count:INT`（1 次）
- `normalize_text:BOOLEAN`（1 次）
- `seed:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto", "S1: 各位观众朋友们晚上好！欢迎收看这场万众期待的“魔都高校德比”，由复旦大学对阵上海交大！我是詹俊，今天在我身旁为大家带来评述的依然是张路指导！\nS2: 嘿嘿，大家好！今天这现场气氛可不一般啊，看台上红蓝两色泾渭分`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
