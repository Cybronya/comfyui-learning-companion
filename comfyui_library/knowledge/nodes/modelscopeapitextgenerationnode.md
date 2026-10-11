# ModelscopeApiTextGenerationNode

## 节点类型

`ModelscopeApiTextGenerationNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `system_prompt:STRING`（1 次）
- `prompt:STRING`（1 次）
- `model_name:STRING`（1 次）
- `max_tokens:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `seed:INT`（1 次）
- `api_token:STRING`（1 次）

## 输出

- `生成文本:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "Qwen/Qwen3-VL-235B-A22B-Instruct", 1000, 0.7, 0.9, 917068475, "randomize", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
