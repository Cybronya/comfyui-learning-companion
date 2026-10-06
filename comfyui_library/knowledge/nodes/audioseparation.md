# AudioSeparation

## 节点类型

`AudioSeparation`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `audio:AUDIO`（2 次）
- `chunk_fade_shape:COMBO`（2 次）
- `chunk_length:FLOAT`（2 次）
- `chunk_overlap:FLOAT`（2 次）

## 输出

- `Bass:AUDIO`（2 次）
- `Drums:AUDIO`（2 次）
- `Other:AUDIO`（2 次）
- `Vocals:AUDIO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["linear", 10, 0.1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
