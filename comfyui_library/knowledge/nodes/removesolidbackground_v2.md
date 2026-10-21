# RemoveSolidBackground_孤海V2

## 节点类型

`RemoveSolidBackground_孤海V2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `颜色阈值:FLOAT`（3 次）
- `边缘采样密度:INT`（3 次）
- `移除扩展:INT`（3 次）
- `模糊半径:FLOAT`（3 次）

## 输出

- `透明背景图像:IMAGE`（3 次）
- `遮罩:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.1, 30, 0, 0.5]`（2 次）
- `[0.23000000000000004, 10, 1, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
