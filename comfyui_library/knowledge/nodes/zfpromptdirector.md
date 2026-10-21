# ZFPromptDirector

## 节点类型

`ZFPromptDirector`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `user_prompt:STRING`（1 次）
- `theme:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `count:INT`（1 次）
- `reference_instruction:STRING`（1 次）
- `reference_creative_json:STRING`（1 次）
- `reference_image:IMAGE`（1 次）
- `enabled:BOOLEAN`（1 次）
- `selection_json:STRING`（1 次）

## 输出

- `writer_system_prompt:STRING`（1 次）
- `writer_tasks:STRING`（1 次）
- `original_prompt:STRING`（1 次）
- `enabled:BOOLEAN`（1 次）
- `selection_json:STRING`（1 次）
- `selection_summary:STRING`（1 次）
- `creation_mode:STRING`（1 次）
- `min_chars:INT`（1 次）
- `max_chars:INT`（1 次）
- `reference_image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "[{\"id\":\"storyboard_sequence__comic_page__1784423161788__b5fc0fe267018\",\"purpose\":\"storyboard_sequence\",\`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
