# RegexStringReplace

## 节点类型

`RegexStringReplace`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `text:STRING`（2 次）
- `pattern:STRING`（2 次）
- `replacement:STRING`（2 次）
- `case_insensitive:BOOLEAN`（2 次）
- `test_mode:BOOLEAN`（2 次）

## 输出

- `STRING:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[\\s\\S]*\"Positive\":\"(.*?)\"[\\s\\S]*", "\\1", false, false]`（1 次）
- `["[\\s\\S]*\"Negative\":\"(.*?)\"[\\s\\S]*", "\\1", false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
