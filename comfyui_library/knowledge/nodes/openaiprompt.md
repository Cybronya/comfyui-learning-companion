# OpenAiPrompt

## 节点类型

`OpenAiPrompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `messages:LIST`（1 次）
- `server_url:STRING`（1 次）
- `api_key:STRING`（1 次）
- `model_name:STRING`（1 次）
- `system_prompt:STRING`（1 次）
- `text:STRING`（1 次）

## 输出

- `结果:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["https://ai.t8star.org/v1", "sk-FeUzy0dA8hLqWkTDMiG6vz9w1y7ztM8cgOzw3HPs5AE9LIDL", "gpt-image-2-all", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
