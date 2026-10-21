# GH_MaskGrowthBlur

## 节点类型

`GH_MaskGrowthBlur`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `遮罩:MASK`（2 次）
- `生长百分比:FLOAT`（2 次）
- `模糊百分比:FLOAT`（2 次）
- `填充孔洞:BOOLEAN`（2 次）
- `圆角模式:BOOLEAN`（2 次）

## 输出

- `遮罩:MASK`（2 次）
- `反转遮罩:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[-0.1, 0, false, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
