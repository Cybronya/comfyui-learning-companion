# H3VideoPromptPlan

## 节点类型

`H3VideoPromptPlan`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `common:STRING`（2 次）
- `segments:STRING`（2 次）
- `repeat_last:BOOLEAN`（2 次）
- `start_segment:INT`（2 次）

## 输出

- `提示词:H3_PROMPTS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["subject_definitions:\n<Subject 1> is Lin Zhixia, the 28-year-old adult Chinese woman in <Picture 1>. Preserve her face`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
