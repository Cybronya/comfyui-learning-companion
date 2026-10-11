# Remove Text

## 节点类型

`Remove Text`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `Text:STRING`（9 次）
- `Opening_tag:STRING`（9 次）
- `Closing_tag:STRING`（9 次）
- `Open_tag_instance:INT`（9 次）
- `Close_tag_instance:INT`（9 次）
- `Remove_tags:BOOLEAN`（9 次）
- `Pass_Through_on_error:BOOLEAN`（9 次）

## 输出

- `Text:STRING`（9 次）
- `Removed_text:STRING`（9 次）
- `Troubleshooting:STRING`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[":\"", "\"", 1, 1, true, true]`（3 次）
- `["：“", "”", 1, 1, true, true]`（3 次）
- `["\"", "\"", 1, 1, true, true]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
