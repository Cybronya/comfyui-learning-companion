# ModelScopeVisionPromptInversion_Sevr

## 节点类型

`ModelScopeVisionPromptInversion_Sevr`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `prompt_text:STRING`（1 次）
- `model_name:COMBO`（1 次）
- `api_key:STRING`（1 次）
- `custom_model:STRING`（1 次）

## 输出

- `prompt:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["详细描述这幅图像内容，要求清晰、准确、全面", "Qwen/Qwen3-VL-235B-A22B-Instruct", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
