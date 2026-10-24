# Overlay Text

## 节点类型

`Overlay Text`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（12 次）
- `text_block_1:TEXT_BLOCK`（12 次）
- `align:COMBO`（12 次）
- `justify:COMBO`（12 次）
- `line_spacing:INT`（12 次）
- `position_x:INT`（12 次）
- `position_y:INT`（12 次）
- `rotation_angle:FLOAT`（12 次）
- `rotation_options:COMBO`（12 次）
- `text_block_2:TEXT_BLOCK`（12 次）

## 输出

- `image:IMAGE`（12 次）
- `text_mask:MASK`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["bottom", "center", 0, 0, -50, 0, "text center", ""]`（12 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
