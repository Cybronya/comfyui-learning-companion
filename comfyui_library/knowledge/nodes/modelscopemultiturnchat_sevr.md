# ModelScopeMultiTurnChat_Sevr

## 节点类型

`ModelScopeMultiTurnChat_Sevr`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `conversation_history:CONVERSATION_HISTORY`（3 次）
- `user_input:STRING`（3 次）
- `system_prompt:STRING`（3 次）
- `model_name:COMBO`（3 次）
- `reset_conversation:BOOLEAN`（3 次）
- `api_key:STRING`（3 次）
- `custom_model:STRING`（3 次）

## 输出

- `回复:STRING`（3 次）
- `对话历史:CONVERSATION_HISTORY`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "你是一个专业书写Ai绘图提示词的顶级专家，当用户请求你扩写、润色提示词时，你应该直接给出符合用户要求的提示词，此外不需任何废话", "Qwen/Qwen3-Next-80B-A3B-Instruct", false, "", "`（1 次）
- `["", "你是一个强大的AI翻译官，当用户请求翻译时，你应该直接给出符合用户要求的提示词，此外不需任何废话", "Qwen/Qwen3-Next-80B-A3B-Instruct", false, "", ""]`（1 次）
- `["", "你是一个强大的AI翻译官，当用户请求翻译时，你应该直接给出符合用户要求的英文提示词，如果用户输入的内容已经是英文，你就直接将英文段落直接输出，此外不需任何废话", "Qwen/Qwen3-Next-80B-A3B-Instruc`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
