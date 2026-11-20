# OpenRouterImageGenerator

## 节点类型

`OpenRouterImageGenerator`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `input_image:IMAGE`（1 次）
- `image_1:IMAGE`（1 次）
- `image_2:IMAGE`（1 次）
- `image_3:IMAGE`（1 次）
- `image_4:IMAGE`（1 次）
- `api_key:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `seed:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `text:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 1088, 1408, 989834183, "randomize", "", "google/gemini-2.5-flash-image-preview:free", "", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
