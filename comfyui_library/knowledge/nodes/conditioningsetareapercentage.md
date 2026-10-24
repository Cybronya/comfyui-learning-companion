# ConditioningSetAreaPercentage

## 节点类型

`ConditioningSetAreaPercentage`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（6 次）
- `width:FLOAT`（3 次）
- `height:FLOAT`（3 次）
- `x:FLOAT`（3 次）
- `y:FLOAT`（3 次）
- `strength:FLOAT`（3 次）

## 输出

- `CONDITIONING:CONDITIONING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 1, 0, 0, 0.2]`（4 次）
- `[0.9, 0.9, 0, 0.05, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
