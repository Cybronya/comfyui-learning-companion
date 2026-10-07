# GLM_Text_Chat

## 节点类型

`GLM_Text_Chat`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `text_system_prompt_preset:COMBO`（1 次）
- `system_prompt_override:STRING`（1 次）
- `api_key:STRING`（1 次）
- `model_name:STRING`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `max_tokens:INT`（1 次）
- `seed:INT`（1 次）
- `text_input:STRING`（1 次）

## 输出

- `response_text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Flux扩写", "", "80a55cfd20b74d2cab825ce365d00120.RLgstkU54NghMky4", "glm-4-flash-250414", 0.9, 0.7, 1024, 12258947155326`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
