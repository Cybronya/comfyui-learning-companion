# API_caption

## 节点类型

`API_caption`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `api_type:COMBO`（1 次）
- `api_url:STRING`（1 次）
- `API_Key:STRING`（1 次）
- `model_name:STRING`（1 次）
- `prompt:STRING`（1 次）
- `output_language:COMBO`（1 次）
- `temperature:FLOAT`（1 次）
- `max_tokens:INT`（1 次）
- `noise_seed:INT`（1 次）

## 输出

- `text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Siliconflow", "<url>", "<your_key>", "Qwen/Qwen3-VL-32B-Instruct", "你是一位专业的AI图像生成提示词工程师。请详细描述这张图像的主体、前景、中景、背景、构图、视觉引导、`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
