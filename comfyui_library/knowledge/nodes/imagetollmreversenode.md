# ImageToLLMReverseNode

## 节点类型

`ImageToLLMReverseNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `reverse_prompt:STRING`（1 次）
- `seed:INT`（1 次）
- `model_type:COMBO`（1 次）
- `api_key:STRING`（1 次）
- `model_name:COMBO`（1 次）
- `temperature:FLOAT`（1 次）
- `max_tokens:INT`（1 次）

## 输出

- `result:STRING`（1 次）
- `api_key:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["请描述这张图像的内容，并根据图像生成详细的提示词。", 511352560, "randomize", "glm", "", "auto", 0.7, 2048]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
