# ChatGPTOpenAI

## 节点类型

`ChatGPTOpenAI`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `api_key:STRING`（1 次）
- `custom_model_name:STRING`（1 次）
- `custom_api_url:STRING`（1 次）
- `prompt:STRING`（1 次）
- `system_content:STRING`（1 次）
- `model:COMBO`（1 次）
- `seed:INT`（1 次）
- `context_size:INT`（1 次）
- `api_url:COMBO`（1 次）

## 输出

- `text:STRING`（1 次）
- `messages:STRING`（1 次）
- `session_history:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "你是专业的影视译制员。你收到的是Whisper按时间顺序切分的英文对话片段。\n规则：\n1. 每个输入片段必须原样输出为JSON数组中独立的一条记录，严禁把多个片段的文本拼接合并到同一条记录里，也严禁拆分成更多条；输出的JSO`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
