# T8_MOSS_SmartLongAudio

## 节点类型

`T8_MOSS_SmartLongAudio`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:T8_MOSS_TRANSCRIBE_MODEL`（1 次）
- `audio:AUDIO`（1 次）
- `prompt:T8_MOSS_PROMPT`（1 次）
- `max_new_tokens_per_chunk:INT`（1 次）
- `target_chunk_minutes:FLOAT`（1 次）
- `max_chunk_minutes:FLOAT`（1 次）
- `overlap_seconds:FLOAT`（1 次）
- `split_strategy:COMBO`（1 次）
- `silence_policy:COMBO`（1 次）
- `vad_aggressiveness:INT`（1 次）

## 输出

- `原音频透传:AUDIO`（1 次）
- `合并原始文本:STRING`（1 次）
- `结构化 JSON:STRING`（1 次）
- `SRT 字幕:STRING`（1 次）
- `ASS 字幕:STRING`（1 次）
- `MOSS_TRANSCRIPT:T8_MOSS_TRANSCRIPT`（1 次）
- `分片报告 JSON:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 8, 10, 1, "vad", "warn", 2, "quality_failure", "read_write", "off", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
