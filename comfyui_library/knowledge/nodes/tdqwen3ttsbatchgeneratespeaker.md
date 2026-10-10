# TDQwen3TTSBatchGenerateSpeaker

## 节点类型

`TDQwen3TTSBatchGenerateSpeaker`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:QWEN3_TTS_MODEL`（1 次）
- `speakers_config:STRING`（1 次）

## 输出

- `speakers:SPEAKER_LIST`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[\n  {\n    \"name\": \"NewSpeaker\",\n    \"instruct\": \"A clear voice\",\n    \"text\": \"Hello world\"\n  }\n]", "`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
