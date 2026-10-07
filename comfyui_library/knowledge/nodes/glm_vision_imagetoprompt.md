# GLM_Vision_ImageToPrompt

## 节点类型

`GLM_Vision_ImageToPrompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_input:IMAGE`（1 次）
- `image_prompt_preset:COMBO`（1 次）
- `prompt_override:STRING`（1 次）
- `model_name:STRING`（1 次）
- `api_key:STRING`（1 次）
- `seed:INT`（1 次）
- `image_url:STRING`（1 次）
- `image_base64:STRING`（1 次）

## 输出

- `GETPrompt:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Flux描述", "", "glm-4.5v", "", 218711105737430, "randomize", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
