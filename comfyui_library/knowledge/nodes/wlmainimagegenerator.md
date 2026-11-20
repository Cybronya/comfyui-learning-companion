# WLMainImageGenerator

## 节点类型

`WLMainImageGenerator`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `product_image:IMAGE`（1 次）
- `product_image_2:IMAGE`（1 次）
- `product_image_3:IMAGE`（1 次）
- `product_image_4:IMAGE`（1 次）
- `api_url:STRING`（1 次）
- `api_key:STRING`（1 次）
- `model_name:STRING`（1 次）
- `product_type:STRING`（1 次）
- `selling_points:STRING`（1 次）
- `design_style:COMBO`（1 次）

## 输出

- `prompts_list:STRING`（1 次）
- `debug_info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["https://open.bigmodel.cn/api/paas/v4/chat/completions", "167a45586c7b425ba3d418dcfc948526.fnjvAMQCkNg8pWYz", "glm-4.6v`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
