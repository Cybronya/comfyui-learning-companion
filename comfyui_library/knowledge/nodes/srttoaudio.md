# SRTToAudio

## 节点类型

`SRTToAudio`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_key:MODEL_KEY`（2 次）
- `voice_clone_prompt:VOICE_CLONE_PROMPT`（2 次）
- `srt_string:STRING`（2 次）
- `language:COMBO`（2 次）
- `tempo_limit:FLOAT`（2 次）
- `mini_gap_ms:INT`（2 次）
- `batch_size:INT`（2 次）
- `model:QWEN3_TTS_MODEL`（2 次）

## 输出

- `audio:AUDIO`（2 次）
- `adjusted_srt:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "auto", 1.5, 100, 10]`（1 次）
- `["1\n00:00:00,080 --> 00:00:00,480\nFirst\n\n2\n00:00:00,480 --> 00:00:01,439\nThis is not an advertisement\n\n3\n00:00:`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
