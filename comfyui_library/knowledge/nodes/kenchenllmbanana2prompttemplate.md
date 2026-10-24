# KenChenLLMBanana2PromptTemplate

## 节点类型

`KenChenLLMBanana2PromptTemplate`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `image_2:IMAGE`（1 次）
- `image_3:IMAGE`（1 次）
- `image_4:IMAGE`（1 次）
- `user_prompt:STRING`（1 次）
- `template_type:COMBO`（1 次）
- `model:COMBO`（1 次）
- `api_provider:COMBO`（1 次）
- `api_key:STRING`（1 次）
- `base_url:STRING`（1 次）

## 输出

- `banana_prompt:STRING`（1 次）
- `raw_response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "生成-逼真场景", "gemini-3-pro-preview [all]", "google", "", "", "Auto", "auto", 2048, 0.7, "high", "Auto", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
