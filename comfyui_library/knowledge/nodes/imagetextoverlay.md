# ImageTextOverlay

## 节点类型

`ImageTextOverlay`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（6 次）
- `text:STRING`（6 次）
- `textbox_width:INT`（6 次）
- `textbox_height:INT`（6 次）
- `max_font_size:INT`（6 次）
- `font:STRING`（6 次）
- `alignment:COMBO`（6 次）
- `color:STRING`（6 次）
- `start_x:INT`（6 次）
- `start_y:INT`（6 次）

## 输出

- `IMAGE:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["A", 200, 200, 80, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "center", "#000000", 0, 0, 0, 80]`（1 次）
- `["B", 200, 200, 80, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "center", "#000000", 0, 0, 0, 80]`（1 次）
- `["C", 200, 200, 80, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "center", "#000000", 0, 0, 0, 80]`（1 次）
- `["D", 200, 200, 80, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "center", "#000000", 0, 0, 0, 80]`（1 次）
- `["E", 200, 200, 80, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "center", "#000000", 0, 0, 0, 80]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
