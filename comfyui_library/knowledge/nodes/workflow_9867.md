# workflow>遮罩逻辑

## 节点类型

`workflow>遮罩逻辑`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `on_false:*`（1 次）
- `value:FLOAT`（1 次）
- `扩展:INT`（1 次）
- `扩展增量:FLOAT`（1 次）
- `倒角:BOOLEAN`（1 次）
- `反转输入:BOOLEAN`（1 次）
- `模糊半径:FLOAT`（1 次）
- `线性透明:FLOAT`（1 次）

## 输出

- `batch_size:INT`（1 次）
- `遮罩:MASK`（1 次）
- `反转遮罩:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 1, 0, true, false, 5, 1, 1, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
