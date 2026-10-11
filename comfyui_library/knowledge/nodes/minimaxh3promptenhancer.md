# MiniMaxH3PromptEnhancer

## 节点类型

`MiniMaxH3PromptEnhancer`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `clip:CLIP`（3 次）
- `clip_tail:MINIMAX_H3_GENERATION_TAIL`（3 次）
- `image:IMAGE`（3 次）
- `manual_prompt:STRING`（3 次）
- `mode_report:STRING`（1 次）
- `system_prompt:STRING`（1 次）
- `max_new_tokens:INT`（1 次）
- `sampling:COMBO`（1 次）
- `temperature:FLOAT`（1 次）
- `top_k:INT`（1 次）

## 输出

- `enhanced_prompt:STRING`（3 次）
- `system_prompt:STRING`（3 次）
- `llm_prompt:STRING`（3 次）
- `enhancer_report:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "You are an expert prompt engineer for MiniMax H3 audiovisual generation. Rewrite the supplied manual H3 draft `（2 次）
- `["", "", "You are an expert prompt engineer for MiniMax H3 audiovisual generation. Rewrite the supplied manual H3 draft `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
