# SoundFlow_Concatenator

## 节点类型

`SoundFlow_Concatenator`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `audio1:AUDIO`（20 次）
- `audio2:AUDIO`（20 次）
- `silence_before:FLOAT`（20 次）
- `silence_between:FLOAT`（20 次）
- `silence_after:FLOAT`（20 次）
- `fade_duration:FLOAT`（20 次）

## 输出

- `concatenated_audio:AUDIO`（20 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 0, 0.01]`（20 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
