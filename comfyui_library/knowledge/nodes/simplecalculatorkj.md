# SimpleCalculatorKJ

## 节点类型

`SimpleCalculatorKJ`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `expression:STRING`（12 次）
- `a:*`（11 次）
- `b:*`（11 次）
- `variables:COMFY_AUTOGROW_V3`（10 次）
- `variables.a:INT,FLOAT,BOOLEAN`（10 次）
- `variables.b:INT,FLOAT,BOOLEAN`（10 次）
- `variables.c:INT,FLOAT,BOOLEAN`（10 次）
- `variables.d:INT,FLOAT,BOOLEAN`（3 次）
- `variables.e:INT,FLOAT,BOOLEAN`（3 次）

## 输出

- `FLOAT:FLOAT`（12 次）
- `INT:INT`（12 次）
- `BOOLEAN:BOOLEAN`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["round(a * b)"]`（3 次）
- `["a"]`（2 次）
- `["round(a * b) + 1"]`（1 次）
- `["a + b + c + d "]`（1 次）
- `["((round(a * b) // 8) * 8) + 1"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
