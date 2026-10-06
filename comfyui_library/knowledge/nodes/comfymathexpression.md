# ComfyMathExpression

## 节点类型

`ComfyMathExpression`

## 分类

Utility

## 作用

计算类节点：数值/表达式运算（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 43 个 workflow 中。

## 输入

- `values.a:FLOAT,INT,BOOLEAN`（126 次）
- `values.b:FLOAT,INT,BOOLEAN`（126 次）
- `expression:STRING`（126 次）
- `values.c:FLOAT,INT,BOOLEAN`（64 次）
- `values.d:FLOAT,INT,BOOLEAN`（15 次）

## 输出

- `FLOAT:FLOAT`（126 次）
- `INT:INT`（126 次）
- `BOOL:BOOLEAN`（126 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["max(5, round(a * 24)) + (5 - (max(5, round(a * 24)) % 17)) % 17"]`（28 次）
- `["max(32, round(a * sqrt(c*1000000/(a*b)) / 32) * 32)"]`（5 次）
- `["max(32, round(b * sqrt(c*1000000/(a*b)) / 32) * 32)"]`（5 次）
- `["(a>0)*(b<=-1)"]`（5 次）
- `["(a<=-1)*b+(a>-1)*a"]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
