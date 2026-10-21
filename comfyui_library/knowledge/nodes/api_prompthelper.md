# API_PromptHelper

## 节点类型

`API_PromptHelper`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `api_type:COMBO`（1 次）
- `api_url:STRING`（1 次）
- `API_Key:STRING`（1 次）
- `model_name:STRING`（1 次）
- `custom_instruction:STRING`（1 次）
- `prompt:STRING`（1 次）
- `output_language:COMBO`（1 次）
- `temperature:FLOAT`（1 次）
- `max_tokens:INT`（1 次）
- `noise_seed:INT`（1 次）

## 输出

- `text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Other", "https://wish.sillydream.top/v1/chat/completions", "sk-T98PjCXtAneAFwqDCNltikL5aFH0XViTDj1klNPLpXM1gtWE", "「XJ`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
