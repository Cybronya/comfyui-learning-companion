# workflow>overlay

## 节点类型

`workflow>overlay`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `ImageResizeAdvanced image:IMAGE`（1 次）
- `optional_mask:MASK`（1 次）
- `x_offset:INT`（1 次）

## 输出

- `int:INT`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `width_num:NUMBER`（1 次）
- `height_num:NUMBER`（1 次）
- `width_float:FLOAT`（1 次）
- `height_float:FLOAT`（1 次）
- `ImageResizeAdvanced width:INT`（1 次）
- `ImageResizeAdvanced height:INT`（1 次）
- `Image Size to Number width_num:NUMBER`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 1792, 1792, "nearest", "keep proportion", "always", 0, "nearest-exact", 0.1, 1792, 1792, "nearest", "keep proportion`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
