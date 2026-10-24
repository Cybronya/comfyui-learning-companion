# Comfyui_gpt_image_1_edit

## 节点类型

`Comfyui_gpt_image_1_edit`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `prompt:STRING`（1 次）
- `api_key:STRING`（1 次）
- `model:STRING`（1 次）
- `n:INT`（1 次）
- `quality:COMBO`（1 次）
- `size:COMBO`（1 次）
- `seed:INT`（1 次）
- `clear_chats:BOOLEAN`（1 次）

## 输出

- `edited_image:IMAGE`（1 次）
- `response:STRING`（1 次）
- `chats:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["让图片1的人物和图2的人物站在一起", "", "gpt-image-1", 1, "low", "auto", 3609062085846, "randomize", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
