# Qwen3VLProcessor

## 节点类型

`Qwen3VLProcessor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（5 次）
- `video:VIDEO`（5 次）
- `text_prompt:STRING`（5 次）
- `model_name:COMBO`（5 次）
- `temperature:FLOAT`（5 次）
- `top_p:FLOAT`（5 次）
- `max_new_tokens:INT`（5 次）
- `min_pixels:INT`（5 次）
- `max_pixels:INT`（5 次）
- `quantization:COMBO`（5 次）

## 输出

- `response:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["by:aijuxi", "Qwen3-VL-8B-Instruct", 0.7, 0.8, 2048, 262144, 786432, "8bit", "eager", 599528815709177, "randomize", 204`（2 次）
- `["判断这是一个抱枕还是挂布\n如果是抱枕、枕头，则输出pillow\n如果是挂布、画布，则输出banner\n结果只输出一个英文单词", "Qwen3-VL-8B-Instruct", 0.6000000000000001, 1, 120`（1 次）
- `["判断这是一个抱枕还是画布\n如果是抱枕、枕头，则输出抱枕\n如果是挂布、画布，则输出画布\n结果只输出一个中文词语", "Qwen3-VL-8B-Instruct", 0.6000000000000001, 1, 12032, 2621`（1 次）
- `["You are a professional visual analyst and reverse-prompt compiler specialized in Krea 2 Raw and Krea 2 Turbo image-to-`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
