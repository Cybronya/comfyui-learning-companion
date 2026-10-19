# QwenImageEngineer

## 节点类型

`QwenImageEngineer`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `gguf_name:COMBO`（1 次）
- `system_prompt:STRING`（1 次）
- `prompt:STRING`（1 次）
- `n_ctx:INT`（1 次）
- `n_gpu_layers:INT`（1 次）
- `max_new_tokens:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `seed:INT`（1 次）

## 输出

- `text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Z-Image-Engineer-V6-Q8_0.gguf", " You are Z-Image-Engineer V6, a prompt-only cinematography and visual-language specia`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
