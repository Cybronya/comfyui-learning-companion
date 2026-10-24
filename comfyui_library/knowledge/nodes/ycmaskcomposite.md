# YCMaskComposite

## 节点类型

`YCMaskComposite`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `destination:MASK`（5 次）
- `source:MASK`（5 次）
- `x:INT`（5 次）
- `y:INT`（5 次）
- `operation:COMBO`（5 次）
- `opacity:FLOAT`（5 次）
- `blend_power:FLOAT`（5 次）

## 输出

- `mask:MASK`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, "add", 1, 0.5]`（4 次）
- `[832, 0, "add", 1, 0.5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
