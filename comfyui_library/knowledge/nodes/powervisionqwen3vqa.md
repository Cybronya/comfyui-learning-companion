# PowerVisionQwen3VQA

## 节点类型

`PowerVisionQwen3VQA`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `source_path:PATH`（1 次）
- `image:IMAGE`（1 次）
- `text:STRING`（1 次）
- `model:COMBO`（1 次）
- `quantization:COMBO`（1 次）
- `keep_model_loaded:BOOLEAN`（1 次）
- `temperature:FLOAT`（1 次）
- `max_new_tokens:INT`（1 次）
- `min_pixels:INT`（1 次）
- `max_pixels:INT`（1 次）

## 输出

- `result:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["你是一位专业的AI图像生成提示词的专家，根据上传的图像精确而详细的反推出提示词。\n要求：输出为中文的结构化提示词，不要出现对图像水印的描述，不要出现无关的文字和符号，不需要总结，不要显示think的过程，直接输出结果，限制在800字以`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
