# DeepExtractV2Node

## 节点类型

`DeepExtractV2Node`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `track:AUDIO`（1 次）
- `out:STRING`（1 次）
- `device:COMBO`（1 次）
- `overlap:FLOAT`（1 次）
- `shifts:INT`（1 次）
- `segment:INT`（1 次）
- `bit_depth:COMBO`（1 次）
- `clip_mode:COMBO`（1 次）
- `audio_format:COMBO`（1 次）
- `mp3_bitrate:INT`（1 次）

## 输出

- `drums:AUDIO`（1 次）
- `bass:AUDIO`（1 次）
- `other:AUDIO`（1 次）
- `vocals:AUDIO`（1 次）
- `derived_stem:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["separated", "cuda", 0.25, 1, 0, "default", "rescale", "wav", 320, 2, 0, true, "add", "", "{track}/{stem}.{ext}"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
