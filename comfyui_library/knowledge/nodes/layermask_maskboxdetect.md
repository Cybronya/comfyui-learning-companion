# LayerMask: MaskBoxDetect

## 节点类型

`LayerMask: MaskBoxDetect`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `mask:MASK`（1 次）

## 输出

- `box_preview:IMAGE`（1 次）
- `x_percent:FLOAT`（1 次）
- `y_percent:FLOAT`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `x:INT`（1 次）
- `y:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["min_bounding_rect", 0, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
