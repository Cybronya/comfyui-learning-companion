# Bjornulf_TextReplace

## 节点类型

`Bjornulf_TextReplace`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `input_text:STRING`（1 次）
- `search_text:STRING`（1 次）
- `replace_text:STRING`（1 次）
- `replace_count:INT`（1 次）
- `use_regex:BOOLEAN`（1 次）
- `case_sensitive:BOOLEAN`（1 次）
- `trim_whitespace:COMBO`（1 次）

## 输出

- `STRING:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["XXX", "316,0", 0, false, true, "none"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
