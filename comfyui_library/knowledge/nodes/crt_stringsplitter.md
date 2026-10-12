# CRT_StringSplitter

## 节点类型

`CRT_StringSplitter`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `text:STRING`（1 次）
- `split_count:INT`（1 次）
- `split_symbol:STRING`（1 次）
- `strip_whitespace:BOOLEAN`（1 次）

## 输出

- `string_1:STRING`（1 次）
- `string_2:STRING`（1 次）
- `string_3:STRING`（1 次）
- `string_4:STRING`（1 次）
- `string_5:STRING`（1 次）
- `string_6:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Paragraph 1...\n\nParagraph 2...", 6, "", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
