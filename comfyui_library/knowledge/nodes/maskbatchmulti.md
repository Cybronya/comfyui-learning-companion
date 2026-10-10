# MaskBatchMulti

## 节点类型

`MaskBatchMulti`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `mask_1:MASK`（3 次）
- `mask_2:MASK`（3 次）
- `inputcount:INT`（3 次）
- `mask_3:MASK`（2 次）
- `mask_4:MASK`（1 次）
- `mask_5:MASK`（1 次）

## 输出

- `masks:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, null]`（1 次）
- `[5, null]`（1 次）
- `[3, null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
