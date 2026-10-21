# Comfly_gpt_image_2

## 节点类型

`Comfly_gpt_image_2`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 14 个 workflow 中。

## 输入

- `image1:IMAGE`（15 次）
- `image2:IMAGE`（15 次）
- `image3:IMAGE`（15 次）
- `image4:IMAGE`（15 次）
- `prompt:STRING`（15 次）
- `api_key:STRING`（15 次）
- `model:COMBO`（15 次）
- `quality:COMBO`（15 次）
- `size:COMBO`（15 次）
- `background:COMBO`（15 次）

## 输出

- `images:IMAGE`（15 次）
- `response:STRING`（15 次）
- `image_urls:STRING`（15 次）
- `chats:STRING`（15 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "gpt-image-2", "auto", "1024x1536", "auto", "png", "auto", 1000862949966294, "randomize", true, 600]`（1 次）
- `["", "", "gpt-image-2", "auto", "auto", "auto", "png", "auto", 670532235260561, "randomize", true, 600]`（1 次）
- `["将图1中间的男生换成图2的女生", "", "gpt-image-2", "high", "auto", "auto", "png", "auto", 291653643459978, "randomize", true, 600]`（1 次）
- `["", "", "gpt-image-2", "auto", "auto", "auto", "png", "auto", 909721161687376, "randomize", true, 600]`（1 次）
- `["", "", "gpt-image-2", "auto", "auto", "auto", "png", "auto", 992403479829740, "randomize", true, 600, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
