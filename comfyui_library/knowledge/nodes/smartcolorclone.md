# SmartColorClone

## 节点类型

`SmartColorClone`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `reference:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `reference_mask:MASK`（1 次）
- `strength:FLOAT`（1 次）
- `auto_skip:BOOLEAN`（1 次）

## 输出

- `cloned_image:IMAGE`（1 次）
- `color_diff:FLOAT`（1 次）
- `debug_info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.30000000000000004, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
