# HiggsAudio

## 节点类型

`HiggsAudio`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `MODEL_PATH:MODEL`（1 次）
- `AUDIO_TOKENIZER_PATH:AUDIOTOKENIZER`（1 次）
- `system_prompt:SYSTEMPROMPT`（1 次）
- `reference_audio:AUDIO`（1 次）
- `prompt:STRING`（1 次）

## 输出

- `output:AUDIO`（1 次）
- `used_voice_info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 1024, 0.3, 0.95, 50, "auto", "vex", "", "auto"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
