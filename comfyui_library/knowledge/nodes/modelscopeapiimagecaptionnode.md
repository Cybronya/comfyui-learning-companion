# ModelscopeApiImageCaptionNode

## 节点类型

`ModelscopeApiImageCaptionNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `api_token:STRING`（2 次）
- `model_name:STRING`（2 次）
- `prompt:STRING`（2 次）
- `max_tokens:INT`（2 次）
- `temperature:FLOAT`（2 次）

## 输出

- `图片描述:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ms-84ae0d14-1d84-4b96-8cae-a1df0b3afeaa", "Qwen/Qwen3-VL-235B-A22B-Instruct", "详细描述这张图片的内容，包括主体、背景、颜色、动作，神态，姿态，服装等信息，但`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
