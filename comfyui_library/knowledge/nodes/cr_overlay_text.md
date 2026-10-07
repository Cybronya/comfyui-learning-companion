# CR Overlay Text

## 节点类型

`CR Overlay Text`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `position_x:INT`（1 次）
- `position_y:INT`（1 次）
- `text:STRING`（1 次）
- `font_size:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `show_help:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "阿里妈妈数黑体 Bold.ttf", 100, "black", "top", "left", 0, 0, 500, 513, 0, "text center", "#000000"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
