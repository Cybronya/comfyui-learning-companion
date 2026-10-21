# image_math_value

## 节点类型

`image_math_value`

## 分类

Utility

## 作用

计算类节点：数值/表达式运算（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `a:IMAGE`（2 次）
- `b:IMAGE`（2 次）
- `c:MASK`（2 次）
- `d:MASK`（2 次）
- `expression:STRING`（2 次）
- `clamp:BOOLEAN`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `shape:LIST`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["a+b", true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
