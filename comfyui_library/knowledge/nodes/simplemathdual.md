# SimpleMathDual+

## 节点类型

`SimpleMathDual+`

## 分类

Utility

## 作用

计算类节点：数值/表达式运算（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 12 个 workflow 中。

## 输入

- `a:*`（13 次）
- `b:*`（13 次）
- `c:*`（13 次）
- `d:*`（13 次）
- `value_1:STRING`（13 次）
- `value_2:STRING`（13 次）

## 输出

- `int_1:INT`（13 次）
- `float_1:FLOAT`（13 次）
- `int_2:INT`（13 次）
- `float_2:FLOAT`（13 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["((a*min(1,2048/max(a,b))+15)//16)*16", "((b*min(1,2048/max(a,b))+15)//16)*16"]`（11 次）
- `["max(32,((a*min(1,2048/max(a,b))+16)//32)*32)", "max(32,((b*min(1,2048/max(a,b))+16)//32)*32)"]`（1 次）
- `["min(a,b)", "max(a,b)"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
