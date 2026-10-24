# Comfly_krea_v2_fal

## 节点类型

`Comfly_krea_v2_fal`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `style_image1:IMAGE`（1 次）
- `style_image2:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `model_size:COMBO`（1 次）
- `style_image_url1:STRING`（1 次）
- `style_image_url2:STRING`（1 次）
- `api_key:STRING`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `creativity:COMBO`（1 次）
- `style_strength:FLOAT`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `response:STRING`（1 次）
- `image_urls:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["将图1换成图2的风格，人物动作不变", "large", "", "", "", "9:16", "medium", 1, 55584, "randomize", "base64", 6, 600, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
