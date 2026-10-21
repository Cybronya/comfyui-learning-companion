# LayerUtility: TextImage

## 节点类型

`LayerUtility: TextImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `size_as:*`（2 次）
- `text:STRING`（2 次）
- `font_file:COMBO`（2 次）
- `spacing:INT`（2 次）
- `leading:INT`（2 次）
- `horizontal_border:FLOAT`（2 次）
- `vertical_border:FLOAT`（2 次）
- `scale:FLOAT`（2 次）
- `variation_range:INT`（2 次）
- `variation_seed:INT`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Text", "微软雅黑.ttf", 0, 0, 1.2000000000000002, 5, 60.000000000000014, 0, 123, "horizontal", 1024, 48, "#ffffff", "#00000`（1 次）
- `["Text", "微软雅黑.ttf", 0, 0, 1.2000000000000002, 33.800000000000004, 60.000000000000014, 0, 123, "horizontal", 1024, 48, "`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
