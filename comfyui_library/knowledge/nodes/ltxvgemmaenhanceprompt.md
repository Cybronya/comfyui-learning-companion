# LTXVGemmaEnhancePrompt

## 节点类型

`LTXVGemmaEnhancePrompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）
- `image:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `system_prompt:STRING`（2 次）
- `max_tokens:INT`（2 次）
- `bypass_i2v:BOOLEAN`（2 次）
- `seed:INT`（2 次）

## 输出

- `enhanced_prompt:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "You are a Creative Assistant writing concise, action-focused image-to-video prompts. Given an image (first frame) `（1 次）
- `["", "You are a Creative Assistant. Given a user's raw input prompt describing a scene or concept, expand it into a deta`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
