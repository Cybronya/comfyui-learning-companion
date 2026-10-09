# LayerUtility: SimpleTextImage

## 节点类型

`LayerUtility: SimpleTextImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `size_as:*`（1 次）
- `text:STRING`（1 次）
- `font_file:COMBO`（1 次）
- `align:COMBO`（1 次）
- `char_per_line:INT`（1 次）
- `leading:INT`（1 次）
- `font_size:INT`（1 次）
- `text_color:STRING`（1 次）
- `stroke_width:INT`（1 次）
- `stroke_color:STRING`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["text", "Alibaba-PuHuiTi-Heavy.ttf", "center", 80, 8, 72, "#FFFFFF", 0, "#FF8000", 0, 0, 512, 512]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
