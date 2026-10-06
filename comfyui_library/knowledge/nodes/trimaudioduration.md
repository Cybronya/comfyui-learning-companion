# TrimAudioDuration

## 节点类型

`TrimAudioDuration`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 18 个 workflow 中。

## 输入

- `audio:AUDIO`（39 次）
- `start_index:FLOAT`（39 次）
- `duration:FLOAT`（39 次）

## 输出

- `AUDIO:AUDIO`（39 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 15]`（17 次）
- `[0, 2048]`（12 次）
- `[0, 2]`（3 次）
- `[-0.9167, 1]`（2 次）
- `[0, 5.000000000000001]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
