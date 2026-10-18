# BreezeTTS2VoiceClone

## 节点类型

`BreezeTTS2VoiceClone`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `breeze_model:BREEZE_TTS2_MODEL`（7 次）
- `reference_audio:AUDIO`（7 次）
- `text:STRING`（7 次）
- `reference_text:STRING`（7 次）
- `cfg_scale:FLOAT`（7 次）
- `max_new_tokens:INT`（7 次）
- `temperature:FLOAT`（7 次）
- `top_k:INT`（7 次）
- `top_p:FLOAT`（7 次）
- `repetition_penalty:FLOAT`（7 次）

## 输出

- `audio:AUDIO`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 1, 1500, 0.9, 50, 1, 1.1, 0.9, 50, 1, 1526248169, "fixed"]`（4 次）
- `["[笑] 拜拜了您呐！我就不在这里陪您啦~。", "This is the exact transcript of the reference audio.", 1, 1500, 0.9, 50, 1, 1.1, 0.9, 50, 1, `（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
