# QWEN3_Text

## 节点类型

`QWEN3_Text`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:COMBO`（1 次）
- `user_prompt:STRING`（1 次）
- `system_prompt:STRING`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `seed:INT`（1 次）
- `conversation_history:STRING`（1 次）
- `api_key:STRING`（1 次）

## 输出

- `response:STRING`（1 次）
- `conversation_history:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen3-max", "你好,请介绍一下你自己", "You are a helpful assistant.", 0.7, 0.8, 894, "fixed", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
