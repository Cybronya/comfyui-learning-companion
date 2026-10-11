# Text to Image Generator

## 节点类型

`Text to Image Generator`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `font:TEXT_GRAPHIC_ELEMENT`（1 次）
- `canvas:CANVAS_SETTINGS`（1 次）
- `transcription:TRANSCRIPTION`（1 次）
- `highlight_font:TEXT_GRAPHIC_ELEMENT`（1 次）
- `text:STRING`（1 次）
- `frame_count:INT`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `framestamps_string:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["THE FUTURE OF TEXT IS MOTION", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
