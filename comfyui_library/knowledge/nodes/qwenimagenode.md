# QwenImageNode

## 节点类型

`QwenImageNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prompt:STRING`（1 次）
- `api_token:STRING`（1 次）
- `model:STRING`（1 次）
- `negative_prompt:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `seed:INT`（1 次）
- `steps:INT`（1 次）
- `guidance:FLOAT`（1 次）
- `timeout:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["A beautiful landscape", "ms-b0909217-97be-4528-8db3-f067bae06f62", "Qwen/Qwen-Image", "lowres, bad anatomy, bad hands,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
