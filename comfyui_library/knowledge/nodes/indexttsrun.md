# IndexTTSRun

## 节点类型

`IndexTTSRun`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）
- `text:STRING`（1 次）
- `dialogue_audio_s2:AUDIO`（1 次）
- `version:COMBO`（1 次）
- `top_k:INT`（1 次）
- `top_p:FLOAT`（1 次）
- `temperature:FLOAT`（1 次）
- `num_beams:INT`（1 次）
- `max_mel_tokens:INT`（1 次）
- `max_text_tokens_per_sentence:INT`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["v1.5", 30, 0.8, 1, 3, 784, 94, 4, true, false, false, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
