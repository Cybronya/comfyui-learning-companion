# SaveImageAdvanced

## 节点类型

`SaveImageAdvanced`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 47 个 workflow 中。

## 输入

- `images:IMAGE`（57 次）
- `filename_prefix:STRING`（57 次）
- `format:COMFY_DYNAMICCOMBO_V3`（57 次）
- `format.bit_depth:COMBO`（57 次）
- `format.input_color_space:COMBO`（57 次）

## 输出

- `images:IMAGE`（57 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen_image_2.1", "png", "8-bit", "sRGB"]`（34 次）
- `["ComfyUI", "png", "8-bit", "sRGB"]`（19 次）
- `["Qwen21_Anime_PE_9x16", "png", "8-bit", "sRGB"]`（1 次）
- `["anime10_worlds_20261003/01_magazine", "png", "8-bit", "sRGB"]`（1 次）
- `["image/Qwen_image_2.1", "png", "8-bit", "sRGB"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
