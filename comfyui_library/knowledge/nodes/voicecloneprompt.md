# VoiceClonePrompt

## 节点类型

`VoiceClonePrompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_key:MODEL_KEY`（2 次）
- `ref_audio:AUDIO`（2 次）
- `ref_text:STRING`（2 次）
- `model:QWEN3_TTS_MODEL`（2 次）

## 输出

- `voice_clone_prompt:VOICE_CLONE_PROMPT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Hello everyone. I'm SevenFading. Today I'm sharing an AI image generation tool with you."]`（1 次）
- `["This is a moose, right?\nOh, that's how it works, so it depend on the peak."]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
