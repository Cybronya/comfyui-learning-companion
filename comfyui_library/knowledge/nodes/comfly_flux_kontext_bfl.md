# Comfly_Flux_Kontext_bfl

## 节点类型

`Comfly_Flux_Kontext_bfl`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `input_image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `api_key:STRING`（1 次）
- `seed:INT`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `output_format:COMBO`（1 次）
- `prompt_upsampling:BOOLEAN`（1 次）
- `safety_tolerance:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `image_url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "flux-kontext-pro", "", 449302735, "randomize", "3:4", "png", false, 2]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
