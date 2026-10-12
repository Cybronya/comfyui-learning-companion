# AdjustAudio

## 节点类型

`AdjustAudio`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）
- `volume_factor:FLOAT`（1 次）
- `pitch_shift:INT`（1 次）
- `speed_factor:FLOAT`（1 次）
- `normalize:BOOLEAN`（1 次）
- `add_echo:BOOLEAN`（1 次）
- `gain_in:FLOAT`（1 次）
- `gain_out:FLOAT`（1 次）
- `delays:INT`（1 次）
- `decays:FLOAT`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.30000000000000004, 0, 1, false, false, 0.8, 0.88, 60, 0.4]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
