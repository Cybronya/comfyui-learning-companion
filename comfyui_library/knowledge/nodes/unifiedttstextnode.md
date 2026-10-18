# UnifiedTTSTextNode

## 节点类型

`UnifiedTTSTextNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `TTS_engine:TTS_ENGINE`（2 次）
- `opt_narrator:*`（2 次）
- `text:STRING`（2 次）
- `narrator_voice:COMBO`（2 次）
- `seed:INT`（2 次）
- `enable_chunking:BOOLEAN`（2 次）
- `max_chars_per_chunk:INT`（2 次）
- `chunk_combination_method:COMBO`（2 次）
- `silence_between_chunks_ms:INT`（2 次）
- `enable_audio_cache:BOOLEAN`（2 次）

## 输出

- `audio:AUDIO`（2 次）
- `generation_info:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Hello! This is unified TTS with character switching support.\n[Alice] Hi there! I'm Alice speaking with the selected T`（1 次）
- `["Hello! This is unified TTS with character switching support.\n[Alice] Hi there! I'm Alice speaking with the selected T`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
