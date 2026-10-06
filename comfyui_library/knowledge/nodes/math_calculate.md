# math_calculate

## 节点类型

`math_calculate`

## 分类

Utility

## 作用

计算类节点：数值/表达式运算（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `a:*`（33 次）
- `b:*`（33 次）
- `c:*`（33 次）
- `preset:COMBO`（33 次）
- `expression:STRING`（33 次）

## 输出

- `float_result:FLOAT`（33 次）
- `int_result:INT`（33 次）
- `bool_result:BOOLEAN`（33 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["a - b", ""]`（12 次）
- `["floor(a÷b)", ""]`（6 次）
- `["ceil(a÷b)", ""]`（6 次）
- `["a > b", ""]`（6 次）
- `["sqrt(a)", ""]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
