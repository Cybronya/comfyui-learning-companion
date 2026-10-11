# Color Correct (mtb)

## 节点类型

`Color Correct (mtb)`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（6 次）
- `mask:MASK`（6 次）
- `clamp:COMBO`（6 次）
- `gamma:FLOAT`（6 次）
- `contrast:FLOAT`（6 次）
- `exposure:FLOAT`（6 次）
- `offset:FLOAT`（6 次）
- `hue:FLOAT`（6 次）
- `saturation:FLOAT`（6 次）
- `value:FLOAT`（6 次）

## 输出

- `IMAGE:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 0.5, 1, 0, 0, 0, 1, 1]`（3 次）
- `[true, 2, 1, 0, 0, 0, 1, 1]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
