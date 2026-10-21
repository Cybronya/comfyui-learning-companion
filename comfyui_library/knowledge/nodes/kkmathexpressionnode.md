# kkMathExpressionNode

## 节点类型

`kkMathExpressionNode`

## 分类

Utility

## 作用

计算类节点：数值/表达式运算（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `expression:STRING`（2 次）
- `a:FLOAT`（2 次）
- `b:FLOAT`（2 次）
- `c:FLOAT`（2 次）
- `d:FLOAT`（2 次）
- `round_decimals:INT`（2 次）

## 输出

- `float_result:FLOAT`（2 次）
- `int_result:INT`（2 次）
- `string_result:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["a + b", 0, 0, 0, 0, 6]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
