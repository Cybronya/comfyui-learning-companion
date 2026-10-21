# QwenImage21_T2IPromptRewrite

## 节点类型

`QwenImage21_T2IPromptRewrite`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 16 个 workflow 中。

## 输入

- `clip:CLIP`（16 次）
- `prompt:STRING`（16 次）
- `temperature:FLOAT`（16 次）
- `top_p:FLOAT`（16 次）
- `top_k:INT`（16 次）
- `presence_penalty:FLOAT`（16 次）
- `max_new_tokens:INT`（16 次）
- `seed:INT`（16 次）

## 输出

- `positive_prompt:STRING`（16 次）
- `negative_prompt:STRING`（16 次）
- `wh_ratio:STRING`（16 次）
- `thinking:STRING`（16 次）
- `parse_ok:BOOLEAN`（16 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 1, 0.95, 20, 1.5, 4096, 574561962, "randomize"]`（3 次）
- `["", 1, 0.95, 20, 1.5, 16256, 2498179254, "randomize"]`（2 次）
- `["", 1, 0.95, 20, 1.5, 16256, 4224835079, "randomize"]`（2 次）
- `["", 1, 0.95, 20, 1.5, 16256, 647813371, "randomize"]`（2 次）
- `["", 1, 0.95, 20, 1.5, 16256, 1170089479, "randomize"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
