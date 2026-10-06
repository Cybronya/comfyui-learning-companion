# SimplePromptBatcher

## 节点类型

`SimplePromptBatcher`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `prepend:STRING`（3 次）
- `prompts:STRING`（3 次）
- `append:STRING`（3 次）

## 输出

- `prompt:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", ""]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
