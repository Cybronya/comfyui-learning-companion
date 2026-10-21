# TutuGeminiAPI

## 节点类型

`TutuGeminiAPI`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prompt:STRING`（1 次）
- `input_image_1:IMAGE`（1 次）
- `input_image_2:IMAGE`（1 次）
- `input_image_3:IMAGE`（1 次）
- `input_image_4:IMAGE`（1 次）
- `input_image_5:IMAGE`（1 次）
- `api_provider:COMBO`（1 次）
- `model:COMBO`（1 次）
- `num_images:INT`（1 次）
- `temperature:FLOAT`（1 次）

## 输出

- `generated_images:IMAGE`（1 次）
- `response:STRING`（1 次）
- `image_url:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["OpenRouter", "[OpenRouter] google/gemini-2.5-flash-image-preview", 1, 1, 0.95, 120, "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
