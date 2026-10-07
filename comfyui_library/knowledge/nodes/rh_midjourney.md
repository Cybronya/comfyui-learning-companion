# RH_Midjourney

## 节点类型

`RH_Midjourney`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `ref_image:IMAGE`（4 次）
- `prompt:STRING`（3 次）
- `reference_type:COMBO`（1 次）
- `active_weight:FLOAT`（1 次）
- `model_selected:COMBO`（1 次）
- `aspect_rate:COMBO`（1 次）
- `seed:INT`（1 次）
- `upscale_selection:COMBO`（1 次）

## 输出

- `grid_image:IMAGE`（4 次）
- `upscaled_image_1:IMAGE`（4 次）
- `upscaled_image_2:IMAGE`（4 次）
- `upscaled_image_3:IMAGE`（4 次）
- `upscaled_image_4:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["a beautiful girl", "--oref", 500, "Midjourney V7", "auto", 143738199, "randomize", "1"]`（1 次）
- `["a beautiful gril", "--oref", 100, "Midjourney V7", "9:16", 106607641, "randomize", "1"]`（1 次）
- `["a beautiful gril", "--oref", 100, "Midjourney V7", "3:4", 2820212882, "randomize", "1"]`（1 次）
- `["a beautiful cat", "--oref", 100, "Midjourney V7", "3:4", 3704510034, "randomize", "none"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
