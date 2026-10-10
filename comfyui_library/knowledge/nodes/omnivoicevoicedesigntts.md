# OmniVoiceVoiceDesignTTS

## 节点类型

`OmniVoiceVoiceDesignTTS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:COMBO`（1 次）
- `text:STRING`（1 次）
- `voice_instruct:STRING`（1 次）
- `steps:INT`（1 次）
- `speed:FLOAT`（1 次）
- `duration:FLOAT`（1 次）
- `device:COMBO`（1 次）
- `dtype:COMBO`（1 次）
- `attention:COMBO`（1 次）
- `seed:INT`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["OmniVoice", "Hello! This is a test of voice design with OmniVoice.", "female, low pitch", 32, 1, 0, "auto", "auto", "a`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
