# ElevenLabsTextToSpeech

## 节点类型

`ElevenLabsTextToSpeech`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `voice:ELEVENLABS_VOICE`（3 次）
- `text:STRING`（1 次）

## 输出

- `AUDIO:AUDIO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Now, you can generate voice using the ElevenLabs Text - to - Speech node. You can also use your own voice to create a `（1 次）
- `["[low, gravelly voice, unhurried] The lighthouse was dark for eleven years... until tonight.\n\n[quietly, with wonder] `（1 次）
- `["", 0.5, "auto", "eleven_v3", 1, 0.75, "", 3333, "fixed", "mp3_44100_192"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
