# JoyAI_Image_Understand

## 节点类型

`JoyAI_Image_Understand`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `max_new_tokens:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `top_k:INT`（1 次）
- `infer_device:COMBO`（1 次）

## 输出

- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["用中文描述这张图片的风格和画面的内容还有构图。", 2048, 0.7, 0.8, 50, "cuda"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
