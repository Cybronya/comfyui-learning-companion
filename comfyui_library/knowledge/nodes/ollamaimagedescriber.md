# OllamaImageDescriber

## 节点类型

`OllamaImageDescriber`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `structured_output_format:STRING`（1 次）
- `model:COMBO`（1 次）
- `custom_model:STRING`（1 次）
- `api_host:STRING`（1 次）
- `timeout:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `top_k:INT`（1 次）
- `top_p:FLOAT`（1 次）
- `repeat_penalty:FLOAT`（1 次）

## 输出

- `result:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["llava:7b-v1.6-vicuna-q2_K (Q2_K, 3.2GB)", "", "http://localhost:11434", 300, 0.2, 40, 0.9, 1.1, 42, 2048, 200, -1, "Yo`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
