# MaskToSEGS_for_AnimateDiff

## 节点类型

`MaskToSEGS_for_AnimateDiff`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `mask:MASK`（3 次）
- `combined:BOOLEAN`（3 次）
- `crop_factor:FLOAT`（3 次）
- `bbox_fill:BOOLEAN`（3 次）
- `drop_size:INT`（3 次）
- `contour_fill:BOOLEAN`（3 次）

## 输出

- `SEGS:SEGS`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, 3, true, 50, true]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
