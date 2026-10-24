# mask_and_mask_math

## 节点类型

`mask_and_mask_math`

## 分类

Utility

## 作用

计算类节点：数值/表达式运算（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `mask1:MASK`（1 次）
- `mask2:MASK`（1 次）
- `operation:COMBO`（1 次）
- `algorithm:COMBO`（1 次）
- `invert_mask1:BOOLEAN`（1 次）
- `invert_mask2:BOOLEAN`（1 次）

## 输出

- `mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["-", "cv2", false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
