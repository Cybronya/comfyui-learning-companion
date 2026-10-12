# VibeVoiceTranscribe

## 节点类型

`VibeVoiceTranscribe`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vibevoice_model:VIBEVOICE_MODEL`（1 次）
- `audio:AUDIO`（1 次）
- `max_new_tokens:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `repetition_penalty:FLOAT`（1 次）
- `num_beams:INT`（1 次）
- `seed:INT`（1 次）
- `context_info:STRING`（1 次）

## 输出

- `srt_content:STRING`（1 次）
- `json_content:STRING`（1 次）
- `raw_text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4096, 0, 1, 1, 1, 1, "fixed", "识别此音频中歌曲的歌词内容，并生成每句歌词对应的开始时间和结束时间戳"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
