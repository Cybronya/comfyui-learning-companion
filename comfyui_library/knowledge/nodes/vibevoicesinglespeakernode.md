# VibeVoiceSingleSpeakerNode

## 节点类型

`VibeVoiceSingleSpeakerNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `voice_to_clone:AUDIO`（1 次）
- `lora:LORA_CONFIG`（1 次）
- `text:STRING`（1 次）
- `model:COMBO`（1 次）
- `attention_type:COMBO`（1 次）
- `quantize_llm:COMBO`（1 次）
- `free_memory_after_generate:BOOLEAN`（1 次）
- `diffusion_steps:INT`（1 次）
- `seed:INT`（1 次）
- `cfg_scale:FLOAT`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "VibeVoice-Large", "auto", "full precision", true, 20, 42, "fixed", 1.3, false, 0.95, 0.95, 250, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
