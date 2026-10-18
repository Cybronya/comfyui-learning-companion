# VoiceEffects

## 节点类型

`VoiceEffects`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）
- `room_size:FLOAT`（1 次）
- `damping:FLOAT`（1 次）
- `cutoff_freq:FLOAT`（1 次）
- `filter_type:COMBO`（1 次）
- `vibrato_freq:FLOAT`（1 次）
- `vibrato_depth:FLOAT`（1 次）
- `shift_factor:FLOAT`（1 次）
- `delay_time:FLOAT`（1 次）
- `decay:FLOAT`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 800, "highpass", 1, 0, 1, 0.1, 0.1, 1, 0.1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
