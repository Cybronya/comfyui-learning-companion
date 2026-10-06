# MathExpression|pysssss

## 节点类型

`MathExpression|pysssss`

## 分类

Utility

## 作用

计算类节点：数值/表达式运算（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `a:INT,FLOAT,IMAGE,LATENT`（6 次）
- `b:INT,FLOAT,IMAGE,LATENT`（6 次）
- `c:INT,FLOAT,IMAGE,LATENT`（6 次）
- `expression:INT,FLOAT,IMAGE,LATENT`（6 次）

## 输出

- `INT:INT`（6 次）
- `FLOAT:FLOAT`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["a*1"]`（3 次）
- `["(a+1535)//1536+int(a%1536==0)"]`（2 次）
- `["a-2"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
