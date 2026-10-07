# LayerUtility: PhiPrompt

## 节点类型

`LayerUtility: PhiPrompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `user_prompt:STRING`（2 次）
- `system_prompt:STRING`（2 次）

## 输出

- `text:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Phi-3.5-mini-instruct", "cuda", "fp16", false, "You are an AI drawing assistant with rich imagination, good at describ`（1 次）
- `["Phi-3.5-vision-instruct", "cuda", "fp16", true, "You are a helpful AI assistant.", "You are an imaginative artificial `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
