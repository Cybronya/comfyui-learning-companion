# PenguinTextOnImage

## 节点类型

`PenguinTextOnImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `text:STRING`（4 次）
- `x_pct:INT`（4 次）
- `y_pct:INT`（4 次）
- `h_anchor:COMBO`（4 次）
- `v_anchor:COMBO`（4 次）
- `offset_x:INT`（4 次）
- `offset_y:INT`（4 次）
- `font_size:INT`（4 次）
- `font_file:COMBO`（4 次）

## 输出

- `IMAGE:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 13, 80, "left", "top", 0, 0, 68, "思源黑体SourceHanSansCN-Regular.otf", "#000000", 0.5, false, "#000000", "#000000", 0,`（1 次）
- `["", 33, 68, "left", "top", 0, 0, 156, "思源黑体SourceHanSansCN-Bold.otf", "#ffffff", 1, false, "#ff0000", "#0000ff", 0, 0, `（1 次）
- `["", 28, 85, "left", "top", 0, 0, 68, "思源黑体SourceHanSansCN-Regular.otf", "#000000", 0.5, false, "#000000", "#000000", 0,`（1 次）
- `["", 33, 90, "left", "top", 0, 0, 68, "思源黑体SourceHanSansCN-Regular.otf", "#000000", 0.5, false, "#000000", "#000000", 0,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
