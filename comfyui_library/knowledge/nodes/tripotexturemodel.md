# TripoTextureModel

## 节点类型

`TripoTextureModel`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_info:MODEL_INFO`（1 次）
- `image_prompt:IMAGE`（1 次）
- `style_image:IMAGE`（1 次）
- `model_version:COMBO`（1 次）
- `texture:BOOLEAN`（1 次）
- `pbr:BOOLEAN`（1 次）
- `texture_seed:INT`（1 次）
- `texture_quality:COMBO`（1 次）
- `texture_alignment:COMBO`（1 次）
- `text_prompt:STRING`（1 次）

## 输出

- `model_file:STRING`（1 次）
- `model_info:MODEL_INFO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["v3.0-20250812", true, true, 42, "standard", "original_image", "", "", false, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
