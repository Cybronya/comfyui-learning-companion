# ZVH3PromptInput

## 节点类型

`ZVH3PromptInput`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `media_project:ZV_MEDIA_PROJECT`（1 次）
- `trigger_words:STRING`（1 次）
- `prompt_text:STRING`（1 次）
- `interview_json:STRING`（1 次）

## 输出

- `prompt:STRING`（1 次）
- `material_context_json:STRING`（1 次）
- `duration_seconds:FLOAT`（1 次）
- `interview_json:STRING`（1 次）
- `human_report:STRING`（1 次）
- `ready:BOOLEAN`（1 次）
- `reference_plan:ZV_H3_REFERENCE_PLAN`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "subject_definitions:\n<Picture 1> is the brand-poster composition reference for [Shot 1] and [Shot 5], with the ce`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
