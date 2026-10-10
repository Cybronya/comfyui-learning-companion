# FB_Qwen3TTSVoiceClone

## 节点类型

`FB_Qwen3TTSVoiceClone`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `ref_audio:AUDIO`（1 次）
- `voice_clone_prompt:VOICE_CLONE_PROMPT`（1 次）
- `config:TTS_CONFIG`（1 次）
- `target_text:STRING`（1 次）
- `model_choice:COMBO`（1 次）
- `device:COMBO`（1 次）
- `precision:COMBO`（1 次）
- `language:COMBO`（1 次）
- `ref_text:STRING`（1 次）
- `seed:INT`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Good one. Okay, fine, I'm just gonna leave this sock monkey here. Goodbye.", "1.7B", "auto", "bf16", "Auto", "", 42, "`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
