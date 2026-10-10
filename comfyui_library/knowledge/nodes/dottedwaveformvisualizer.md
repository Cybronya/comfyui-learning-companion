# DottedWaveformVisualizer

## 节点类型

`DottedWaveformVisualizer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `size:INT`（1 次）
- `spacing:INT`（1 次）
- `dot_color:STRING`（1 次）
- `background_color:STRING`（1 次）
- `animation_style:COMBO`（1 次）
- `max_height:INT`（1 次）
- `fps:INT`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `audio:AUDIO`（1 次）
- `fps_output:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1280, 720, 10, 15, "#00FFFF", "#000000", "scrolling", 100, 10, 0, "5_levels", 1, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
