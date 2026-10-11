# Prompt_Edit

## 节点类型

`Prompt_Edit`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `text:STRING`（1 次）
- `edited_text_widget:STRING`（1 次）

## 输出

- `edited_text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["For the target video, at 0.00 seconds into the target video, <P> (from [Shot 1]) is fully referenced.\n\nsubject_defin`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
