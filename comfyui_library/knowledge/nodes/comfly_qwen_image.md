# Comfly_qwen_image

## 节点类型

`Comfly_qwen_image`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prompt:STRING`（1 次）
- `size:COMBO`（1 次）
- `Custom_size:STRING`（1 次）
- `model:COMBO`（1 次）
- `num_images:COMBO`（1 次）
- `api_key:STRING`（1 次）
- `num_inference_steps:INT`（1 次）
- `seed:INT`（1 次）
- `guidance_scale:FLOAT`（1 次）
- `enable_safety_checker:BOOLEAN`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `response:STRING`（1 次）
- `image_url:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "768x1024", "Enter custom size (e.g. 1280x720)", "qwen-image", 1, "", 30, 1028388304429454, "fixed", 2.5, true, "",`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
