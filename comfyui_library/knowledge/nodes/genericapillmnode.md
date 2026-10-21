# GenericAPILLMNode

## 节点类型

`GenericAPILLMNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `api_url:STRING`（1 次）
- `api_key:STRING`（1 次）
- `model:STRING`（1 次）
- `system_prompt:STRING`（1 次）
- `user_prompt:STRING`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `max_tokens:INT`（1 次）
- `presence_penalty:FLOAT`（1 次）
- `frequency_penalty:FLOAT`（1 次）

## 输出

- `response:STRING`（1 次）
- `raw_response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["https://api.deepseek.com", "sk-191496b2d64f40e0a15b25b542098086", "deepseek-v4-pro", "你是一个创意美食摄影专家，擅长为「巨物美食」系列撰写中文提示词。`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
