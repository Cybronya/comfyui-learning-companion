# OmniVoiceVoiceCloneTTS

## 节点类型

`OmniVoiceVoiceCloneTTS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `ref_audio:AUDIO`（7 次）
- `whisper_model:WHISPER_ASR`（7 次）
- `model:COMBO`（7 次）
- `text:STRING`（7 次）
- `ref_text:STRING`（7 次）
- `steps:INT`（7 次）
- `speed:FLOAT`（7 次）
- `duration:FLOAT`（7 次）
- `device:COMBO`（7 次）
- `dtype:COMBO`（7 次）

## 输出

- `audio:AUDIO`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["OmniVoice-bf16 (auto download)", "prompt", "", 32, 2, 0.1, 1, 0, "auto", 0, "auto", 818291550, "randomize"]`（1 次）
- `["OmniVoice", "prompt", "", 32, 2, 0.1, "auto", "auto", "auto", 776195869, "randomize", false, 100]`（1 次）
- `["OmniVoice-bf16", "", "", 32, 1, 0, "auto", "auto", "auto", 1060819297, "randomize", false, 100]`（1 次）
- `["OmniVoice-bf16", "", "", 32, 1, 0, "auto", "auto", "auto", 485393970, "randomize", false, 100]`（1 次）
- `["OmniVoice-bf16", "", "", 32, 1, 0, "auto", "auto", "auto", 179858329, "randomize", false, 100]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
