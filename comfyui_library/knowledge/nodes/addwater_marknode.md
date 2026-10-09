# AddWater_MarkNode

## 节点类型

`AddWater_MarkNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `watermark:IMAGE`（1 次）
- `watermark_mask:MASK`（1 次）
- `image_watermark:BOOLEAN`（1 次）
- `position_X:INT`（1 次）
- `position_Y:INT`（1 次）
- `opacity:FLOAT`（1 次）
- `scale:FLOAT`（1 次）
- `text:STRING`（1 次）
- `text_color:STRING`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `font_path:PATH`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 10, 10, 0.5, 1, "enter text", "#FFFFFF", "blackrumbleregular.ttf"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
