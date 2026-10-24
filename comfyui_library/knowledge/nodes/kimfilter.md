# KimFilter

## 节点类型

`KimFilter`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `UM非锐化掩蔽:FLOAT`（1 次）
- `DCP暗通道先验:FLOAT`（1 次）
- `CLAHE对比度增强限制:FLOAT`（1 次）
- `自然饱和度:FLOAT`（1 次）
- `伽马值:FLOAT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0.10000000000000002, 0, 0.9000000000000001, 0.9500000000000002]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
