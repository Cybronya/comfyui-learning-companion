# Text_Image_Multiline_Zho

## 节点类型

`Text_Image_Multiline_Zho`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `text:STRING`（2 次）
- `selected_font:COMBO`（2 次）
- `align:COMBO`（2 次）
- `wrap:INT`（2 次）
- `graphspace:INT`（2 次）
- `linespace:INT`（2 次）
- `font_size:INT`（2 次）
- `color:COLOR`（2 次）
- `outline_size:INT`（2 次）
- `outline_color:COLOR`（2 次）

## 输出

- `image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ZHOZHOZHO", "Alkatra.ttf", "center", 100, 10, 6, 50, "#fffafa", 0, "blue", 0, 10, 1000, 200, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
