# RegexExtract

## 节点类型

`RegexExtract`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `string:STRING`（10 次）
- `regex_pattern:STRING`（10 次）
- `mode:COMBO`（10 次）
- `case_insensitive:BOOLEAN`（10 次）
- `multiline:BOOLEAN`（10 次）
- `dotall:BOOLEAN`（10 次）
- `group_index:INT`（10 次）

## 输出

- `STRING:STRING`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "^\\s*([^,，(（]+)", "All Matches", true, true, true, 0]`（7 次）
- `["", "\\{.*\\}", "First Match", true, false, true, 1]`（1 次）
- `["", "\"rewritten_prompt\"\\s*:\\s*\"([\\s\\S]*?)\"\\s*,", "First Group", true, false, false, 1]`（1 次）
- `["", "^\\s*([^;；,，(（]+)", "All Matches", true, true, true, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
