# GrowMaskWithBlur

## 节点类型

`GrowMaskWithBlur`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `mask:MASK`（8 次）

## 输出

- `mask:MASK`（8 次）
- `mask_inverted:MASK`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[30, 0.9999999999999999, true, false, 0, 1, 1, false]`（2 次）
- `[40, 0, true, false, 20, 1, 1, false]`（1 次）
- `[15, 0, true, false, 2, 1, 1, false]`（1 次）
- `[-15, 0, true, false, 2, 1, 1, false]`（1 次）
- `[-10, 0, true, false, 2, 1, 1, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
