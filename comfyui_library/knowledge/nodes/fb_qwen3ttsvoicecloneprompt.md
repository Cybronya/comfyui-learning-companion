# FB_Qwen3TTSVoiceClonePrompt

## 节点类型

`FB_Qwen3TTSVoiceClonePrompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `ref_audio:AUDIO`（8 次）
- `ref_text:STRING`（8 次）
- `model_choice:COMBO`（8 次）
- `device:COMBO`（8 次）
- `precision:COMBO`（8 次）
- `attention:COMBO`（8 次）
- `x_vector_only:BOOLEAN`（8 次）
- `unload_model_after_generate:BOOLEAN`（8 次）

## 输出

- `voice_clone_prompt:VOICE_CLONE_PROMPT`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "1.7B", "auto", "bf16", "auto", false, false]`（8 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
