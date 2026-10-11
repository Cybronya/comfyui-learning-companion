# OmniVoiceLongformTTS

## 节点类型

`OmniVoiceLongformTTS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `ref_audio:AUDIO`（1 次）
- `whisper_model:WHISPER_ASR`（1 次）
- `model:COMBO`（1 次）
- `text:STRING`（1 次）
- `ref_text:STRING`（1 次）
- `steps:INT`（1 次）
- `speed:FLOAT`（1 次）
- `duration:FLOAT`（1 次）
- `device:COMBO`（1 次）
- `dtype:COMBO`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["OmniVoice", "", "", 32, 1.4000000000000001, 0, "auto", "auto", "auto", 27123758, "randomize", 70, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
