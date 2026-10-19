# Comfly_gpt_image_1

## 节点类型

`Comfly_gpt_image_1`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `prompt:STRING`（5 次）
- `api_key:STRING`（5 次）
- `model:COMBO`（5 次）
- `n:INT`（5 次）
- `quality:COMBO`（5 次）
- `size:COMBO`（5 次）
- `background:COMBO`（5 次）
- `output_format:COMBO`（5 次）
- `moderation:COMBO`（5 次）
- `seed:INT`（5 次）

## 输出

- `generated_image:IMAGE`（5 次）
- `response:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "gpt-image-1.5", 1, "auto", "auto", "auto", "png", "auto", 279086821056393, "randomize"]`（1 次）
- `["", "", "gpt-image-1.5", 1, "auto", "auto", "auto", "png", "auto", 330530124879612, "randomize"]`（1 次）
- `["", "", "gpt-image-1-mini", 1, "auto", "auto", "auto", "png", "auto", 312536279300684, "randomize"]`（1 次）
- `["", "", "gpt-image-1.5", 1, "auto", "auto", "auto", "png", "auto", 1072243659991981, "randomize"]`（1 次）
- `["", "", "gpt-image-1.5", 1, "auto", "auto", "auto", "png", "auto", 1083436554613798, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
