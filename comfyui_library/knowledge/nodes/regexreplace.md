# RegexReplace

## 节点类型

`RegexReplace`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `string:STRING`（7 次）
- `regex_pattern:STRING`（7 次）
- `replace:STRING`（7 次）
- `case_insensitive:BOOLEAN`（7 次）
- `multiline:BOOLEAN`（7 次）
- `dotall:BOOLEAN`（7 次）
- `count:INT`（7 次）

## 输出

- `STRING:STRING`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "^[\\s\"']+|[\\s\"'.]+$", "", false, false, false, 0]`（5 次）
- `["", "^```(?:json)?\\s*\\n?", "", false, false, false, 1]`（1 次）
- `["", "\\n?```\\s*$", "", false, false, false, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
