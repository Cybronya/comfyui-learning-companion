# BreezeTTS2VoiceDesign

## 节点类型

`BreezeTTS2VoiceDesign`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `breeze_model:BREEZE_TTS2_MODEL`（7 次）
- `text:STRING`（7 次）
- `instruction:STRING`（7 次）
- `cfg_scale:FLOAT`（7 次）
- `max_new_tokens:INT`（7 次）
- `temperature:FLOAT`（7 次）
- `top_k:INT`（7 次）
- `top_p:FLOAT`（7 次）
- `repetition_penalty:FLOAT`（7 次）
- `depth_temperature:FLOAT`（7 次）

## 输出

- `audio:AUDIO`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["(sigh) Welcome aboard. Your journey begins now.", "一个青春明亮的女人的声音，语速稍快", 4, 1500, 0.9, 50, 1, 1.1, 0.9, 50, 1, 1, "fixed`（3 次）
- `["", "", 4, 1500, 0.9, 50, 1, 1.1, 0.9, 50, 1, 1317043110, "randomize"]`（3 次）
- `["", "", 4, 1500, 0.9, 50, 1, 1.1, 0.9, 50, 1, 266499245, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
