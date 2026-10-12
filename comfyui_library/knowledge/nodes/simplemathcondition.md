# SimpleMathCondition+

## 节点类型

`SimpleMathCondition+`

## 分类

Utility

## 作用

计算类节点：数值/表达式运算（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `evaluate:*`（3 次）
- `a:*`（3 次）
- `b:*`（3 次）
- `c:*`（3 次）
- `on_true:STRING`（3 次）
- `on_false:STRING`（3 次）

## 输出

- `INT:INT`（3 次）
- `FLOAT:FLOAT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["a", "a+1"]`（1 次）
- `["a", "a+b"]`（1 次）
- `["a", "a-1"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
