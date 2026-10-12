# FL_PromptSelector

## 节点类型

`FL_PromptSelector`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `prepend_text:STRING`（4 次）
- `prompts:STRING`（4 次）
- `append_text:STRING`（4 次）
- `index:INT`（4 次）

## 输出

- `STRING:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "", 0]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
