# Comfly_gpt_image_2_fal

## 节点类型

`Comfly_gpt_image_2_fal`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image1:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `image4:IMAGE`（1 次）
- `mask:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `mode:COMBO`（1 次）
- `api_key:STRING`（1 次）
- `quality:COMBO`（1 次）
- `image_size:COMBO`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `response:STRING`（1 次）
- `image_urls:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["做成一张高质感杂志封面图", "edit", "", "medium", "custom", 1440, 2560, 1, "png", "image_url", 207020781, "randomize", 10, 300, fal`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
