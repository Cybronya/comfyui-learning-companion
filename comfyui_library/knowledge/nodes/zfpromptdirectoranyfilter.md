# ZFPromptDirectorAnyFilter

## 节点类型

`ZFPromptDirectorAnyFilter`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `value:*`（2 次）
- `condition:COMBO`（2 次）
- `output_action:COMBO`（2 次）
- `filter_content:STRING`（2 次）
- `case_sensitive:BOOLEAN`（2 次）

## 输出

- `value:*`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["输入为空", "无输出（None，跳过此路）", "", true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
