# VibeVoiceMultipleSpeakersNode

## 节点类型

`VibeVoiceMultipleSpeakersNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `speaker1_voice:AUDIO`（1 次）
- `speaker2_voice:AUDIO`（1 次）
- `speaker3_voice:AUDIO`（1 次）
- `speaker4_voice:AUDIO`（1 次）
- `lora:LORA_CONFIG`（1 次）
- `text:STRING`（1 次）
- `model:COMBO`（1 次）
- `attention_type:COMBO`（1 次）
- `quantize_llm:COMBO`（1 次）
- `free_memory_after_generate:BOOLEAN`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[1]: 今天晚上吃什么\n[2]: 东北炖母鸡和来自南方的小白鸽\n[3]: 明天晚上吃什么\n[1]: 西湖糖醋鱼", "VibeVoice-Large", "auto", "full precision", true, 20, 1`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
