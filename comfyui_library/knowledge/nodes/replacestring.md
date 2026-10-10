# ReplaceString

## 节点类型

`ReplaceString`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `String:STRING`（19 次）
- `Regex:STRING`（19 次）
- `ReplaceWith:STRING`（19 次）

## 输出

- `STRING:STRING`（19 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "%%TIMINGSEG1%%", "00:00~00:06"]`（11 次）
- `["", "%%TIMINGSEG2%%", "00:06~00:12"]`（1 次）
- `["", "%%PROMPTSEG2%%", "00:06~00:12"]`（1 次）
- `["", "%%PROMPTSEG1%%", "00:00~00:06"]`（1 次）
- `["", "%%PROMPTSEG3%%", "00:12~00:18 "]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
