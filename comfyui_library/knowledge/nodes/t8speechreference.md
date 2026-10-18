# T8SpeechReference

## 节点类型

`T8SpeechReference`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）
- `video:VIDEO`（1 次）
- `provider_config:T8_LLM_PROVIDER_CONFIG`（1 次）
- `mode:COMBO`（1 次）
- `source_mode:COMBO`（1 次）
- `purpose:COMBO`（1 次）
- `provided_text:STRING`（1 次）
- `provided_format:COMBO`（1 次）
- `speaker_map_json:STRING`（1 次）
- `partial_policy:COMBO`（1 次）

## 输出

- `speech_reference:T8_SPEECH_REFERENCE`（1 次）
- `speech_text:STRING`（1 次）
- `timed_transcript_json:STRING`（1 次）
- `subtitles_srt:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Off", "Provided text", "reference", "", "auto", "{}", "reject", "stop", 0, 0, "Auto", "", 0, "mean", 0, 1800]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
