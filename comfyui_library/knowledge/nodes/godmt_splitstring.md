# GODMT_SplitString

## 节点类型

`GODMT_SplitString`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `STRING:STRING`（1 次）
- `delimiter:STRING`（1 次）
- `splitlines:BOOLEAN`（1 次）
- `strip:BOOLEAN`（1 次）

## 输出

- `STRING:STRING`（1 次）
- `LIST:LIST`（1 次）
- `length:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "/n", true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
