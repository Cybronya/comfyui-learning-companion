# PD_Maskfenkai

## 节点类型

`PD_Maskfenkai`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `min_area:INT`（1 次）
- `row_tolerance:INT`（1 次）
- `split_iterations:INT`（1 次）
- `bbox_padding:INT`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `masks:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[10, 50, 0, 8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
