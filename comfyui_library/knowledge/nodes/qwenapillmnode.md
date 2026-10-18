# QwenAPILLMNode

## 节点类型

`QwenAPILLMNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_input:IMAGE`（1 次）
- `api_key:STRING`（1 次）
- `model:COMBO`（1 次）
- `prompt:STRING`（1 次）
- `system_message:STRING`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `max_tokens:INT`（1 次）
- `seed:INT`（1 次）
- `enable_search:BOOLEAN`（1 次）

## 输出

- `generated_text:STRING`（1 次）
- `status_message:STRING`（1 次）
- `is_success:BOOLEAN`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "qwen-plus-latest", "", "", 0.85, 0.8, 1000, 191846792415451, "randomize", true, true, 1, "Native Batch", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
