# GulfSeaImageMergeMask

## 节点类型

`GulfSeaImageMergeMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `背景图:IMAGE`（1 次）
- `覆盖图:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `透明度:FLOAT`（1 次）
- `遮罩扩展:INT`（1 次）
- `模糊半径:INT`（1 次）
- `匹配图像大小:BOOLEAN`（1 次）

## 输出

- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 0, 0, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
