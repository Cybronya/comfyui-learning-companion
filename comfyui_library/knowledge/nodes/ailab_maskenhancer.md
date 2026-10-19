# AILab_MaskEnhancer

## 节点类型

`AILab_MaskEnhancer`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `mask:MASK`（1 次）
- `sensitivity:FLOAT`（1 次）
- `mask_blur:INT`（1 次）
- `mask_offset:INT`（1 次）
- `smooth:FLOAT`（1 次）
- `fill_holes:BOOLEAN`（1 次）
- `invert_output:BOOLEAN`（1 次）

## 输出

- `MASK:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 5, 5, 0, true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
