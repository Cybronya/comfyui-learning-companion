# EasyColorCorrection

## 节点类型

`EasyColorCorrection`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `reference_image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `mode:COMBO`（1 次）
- `reference_strength:FLOAT`（1 次）
- `extract_palette:BOOLEAN`（1 次）
- `lock_input_image:BOOLEAN`（1 次）
- `ai_analysis:BOOLEAN`（1 次）
- `adjust_for_skin_tone:BOOLEAN`（1 次）
- `white_balance_strength:FLOAT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `palette_data:STRING`（1 次）
- `histogram:IMAGE`（1 次）
- `palette_image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Auto", 0.3, false, true, true, true, 0, 0.2, 0.7, 0.6, -0.05, 0.35, 0.25, -0.05, 0, "Anime Moody", 0, 0, 0, 0, 0, 0, 0`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
