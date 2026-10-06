# TextToListNode

## 节点类型

`TextToListNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `text:STRING`（2 次）
- `delimiter:STRING`（2 次）
- `strip_whitespace:BOOLEAN`（2 次）
- `remove_empty:BOOLEAN`（2 次）

## 输出

- `列表:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "\\n", true, true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
