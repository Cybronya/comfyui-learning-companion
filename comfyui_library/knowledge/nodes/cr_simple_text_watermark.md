# CR Simple Text Watermark

## 节点类型

`CR Simple Text Watermark`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（8 次）
- `text:STRING`（8 次）
- `align:COMBO`（8 次）
- `opacity:FLOAT`（8 次）
- `font_name:COMBO`（8 次）
- `font_size:INT`（8 次）
- `font_color:COMBO`（8 次）
- `x_margin:INT`（8 次）
- `y_margin:INT`（8 次）
- `font_color_hex:STRING`（8 次）

## 输出

- `IMAGE:IMAGE`（8 次）
- `show_help:STRING`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Created By Aoibite", "bottom center", 0.5000000000000001, "摄图摩登小方体.TTF", 30, "white", 20, 20, "#000000"]`（4 次）
- `["Z-image Base+Z-image Turbo+SeedVR", "top center", 0.5000000000000001, "摄图摩登小方体.TTF", 30, "white", 20, 10, "#000000"]`（2 次）
- `["Z-image Base+Turbo+Klein+SeedVR", "top center", 0.5000000000000001, "摄图摩登小方体.TTF", 30, "white", 20, 10, "#000000"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
