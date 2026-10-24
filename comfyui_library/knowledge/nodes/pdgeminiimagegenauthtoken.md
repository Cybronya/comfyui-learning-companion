# PDGeminiImageGenAuthToken

## 节点类型

`PDGeminiImageGenAuthToken`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_ref:IMAGE`（1 次）
- `auth_token:STRING`（1 次）
- `prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `resolution:COMBO`（1 次）
- `seed:INT`（1 次）
- `system_prompt:STRING`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "A futuristic city with flying cars", "gemini-2.5-flash-image", "auto", "1K", 172534678286338, "randomize", "You ar`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
