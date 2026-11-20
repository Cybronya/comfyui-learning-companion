# Demucs_Sampler

## 节点类型

`Demucs_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:Demucs_MODEL`（1 次）
- `audio:AUDIO`（1 次）
- `ext:COMBO`（1 次）
- `bits_per_sample:COMBO`（1 次）
- `as_float:COMBO`（1 次）
- `clip_mode:COMBO`（1 次）
- `mp3_bitrate:INT`（1 次）
- `audio_save:BOOLEAN`（1 次）
- `preset:COMBO`（1 次）

## 输出

- `mixed:AUDIO`（1 次）
- `bass:AUDIO`（1 次）
- `drums:AUDIO`（1 次）
- `other:AUDIO`（1 次）
- `vocals:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flac", 24, "float32", "none", 320, false, 2]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
