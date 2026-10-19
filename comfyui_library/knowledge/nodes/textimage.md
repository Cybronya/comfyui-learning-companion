# TextImage

## 节点类型

`TextImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `text:STRING`（2 次）
- `font:COMBO`（2 次）
- `font_size:INT`（2 次）
- `spacing:INT`（2 次）
- `line_spacing:INT`（2 次）
- `padding:INT`（2 次）
- `text_color:STRING`（2 次）
- `vertical:BOOLEAN`（2 次）
- `stroke:BOOLEAN`（2 次）
- `max_characters_per_line:INT`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["炭灰色直筒毛呢裤", "04HomuraM-Medium-2.otf", 100, 12, 12, 8, "#FFFFFF", false, false, 44, 0]`（1 次）
- `["深灰色半高领打底衫", "04HomuraM-Medium-2.otf", 100, 12, 12, 8, "#FFFFFF", false, false, 44, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
