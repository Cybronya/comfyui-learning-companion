# TutuNanaBananaPromptMaster

## 节点类型

`TutuNanaBananaPromptMaster`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `template_selection:COMBO`（1 次）
- `user_idea:STRING`（1 次）
- `language:COMBO`（1 次）
- `detail_level:COMBO`（1 次）
- `camera_control:COMBO`（1 次）
- `lighting_control:COMBO`（1 次）
- `quality_enhancement:BOOLEAN`（1 次）
- `custom_additions:STRING`（1 次）

## 输出

- `optimized_prompt:STRING`（1 次）
- `template_used:STRING`（1 次）
- `optimization_report:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Custom Input", "Imitate the action and clothing style of the person in the given image to create a new look, ensuring `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
