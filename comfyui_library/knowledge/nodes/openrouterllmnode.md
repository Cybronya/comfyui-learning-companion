# OpenRouterLLMNode

## 节点类型

`OpenRouterLLMNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `model.images.image_1:IMAGE`（6 次）
- `model.images.image_2:IMAGE`（6 次）
- `prompt:STRING`（5 次）

## 输出

- `STRING:STRING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "openai/gpt-5.6-luna", "off", 0, "randomize", ""]`（1 次）
- `["", "openai/gpt-5.6-sol", "off", 0, "randomize", ""]`（1 次）
- `["", "openai/gpt-5.6-terra", "off", 0, "randomize", ""]`（1 次）
- `["", "x-ai/grok-4.5", "off", 0, "randomize", ""]`（1 次）
- `["", "moonshotai/kimi-k3", "off", 0, "randomize", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
