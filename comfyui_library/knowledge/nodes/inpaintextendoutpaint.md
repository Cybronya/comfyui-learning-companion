# InpaintExtendOutpaint

## 节点类型

`InpaintExtendOutpaint`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `mask:MASK`（4 次）
- `optional_context_mask:MASK`（4 次）
- `mode:COMBO`（4 次）
- `expand_up_pixels:INT`（4 次）
- `expand_up_factor:FLOAT`（4 次）
- `expand_down_pixels:INT`（4 次）
- `expand_down_factor:FLOAT`（4 次）
- `expand_left_pixels:INT`（4 次）
- `expand_left_factor:FLOAT`（4 次）

## 输出

- `image:IMAGE`（4 次）
- `mask:MASK`（4 次）
- `context_mask:MASK`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["factors", 0, 1, 0, 1, 0, 1, 0, 1]`（3 次）
- `["factors", 0, 1.2000000000000002, 0, 1.2000000000000002, 0, 1.2000000000000002, 0, 1.2000000000000002]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
