# TextSplitJoinByDelimiter

## 节点类型

`TextSplitJoinByDelimiter`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `text:STRING`（18 次）
- `split_delimiter:STRING`（18 次）
- `start_index:INT`（18 次）
- `skip_every:INT`（18 次）
- `max_count:INT`（18 次）
- `join_delimiter:STRING`（18 次）

## 输出

- `list_str:STRING`（18 次）
- `joined_str:STRING`（18 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "spliter", 0, 0, 1, "\\n"]`（9 次）
- `["", "spliter", 1, 0, 1, "\\n"]`（9 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
