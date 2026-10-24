# Comfly_gpt_image_1_edit

## 节点类型

`Comfly_gpt_image_1_edit`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `mask:MASK`（3 次）
- `prompt:STRING`（3 次）
- `api_key:STRING`（3 次）
- `n:INT`（3 次）
- `quality:COMBO`（3 次）
- `size:COMBO`（3 次）
- `seed:INT`（3 次）
- `clear_chats:BOOLEAN`（3 次）
- `background:COMBO`（3 次）

## 输出

- `edited_image:IMAGE`（3 次）
- `response:STRING`（3 次）
- `chats:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "gpt-image-1", 1, "auto", "auto", 121260392441826, "randomize", true, "auto", 100, "png", 5, 900, "low", 0]`（1 次）
- `["女人看向左边", "", "gpt-image-1.5", 1, "low", "auto", 194270412755378, "randomize", true, "auto", 100, "png", 5, 900, "low",`（1 次）
- `["", "", "gpt-image-1.5", 1, "auto", "auto", 625814588659510, "randomize", true, "auto", 100, "png", 5, 900, "low", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
