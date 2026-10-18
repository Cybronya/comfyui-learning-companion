# YuE2ReferenceVoiceCover

## 节点类型

`YuE2ReferenceVoiceCover`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:YUE2_MODEL`（1 次）
- `song_audio:AUDIO`（1 次）
- `reference_voice:AUDIO`（1 次）
- `diffusion_steps:INT`（1 次）
- `timbre_strength:FLOAT`（1 次）
- `auto_match_pitch:BOOLEAN`（1 次）
- `semitone_shift:INT`（1 次）
- `vocal_gain_db:FLOAT`（1 次）
- `accompaniment_gain_db:FLOAT`（1 次）

## 输出

- `audio:AUDIO`（1 次）
- `result:YUE2_RESULT`（1 次）
- `metadata:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[30, 0.7, false, 0, 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
