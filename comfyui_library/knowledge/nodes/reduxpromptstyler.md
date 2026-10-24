# ReduxPromptStyler

## 节点类型

`ReduxPromptStyler`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（5 次）
- `style_model:STYLE_MODEL`（5 次）
- `clip_vision:CLIP_VISION`（5 次）
- `reference_image:IMAGE`（5 次）
- `mask:MASK`（5 次）
- `prompt_influence:FLOAT`（3 次）
- `reference_influence:FLOAT`（3 次）
- `style_grid_size:INT`（2 次）
- `interpolation_mode:COMBO`（2 次）
- `image_processing_mode:COMBO`（2 次）

## 输出

- `CONDITIONING:CONDITIONING`（5 次）
- `IMAGE:IMAGE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 1, 1, "bicubic", "keep aspect ratio", 8]`（1 次）
- `[1, 0.7000000000000001, 1, "bicubic", "keep aspect ratio", 8]`（1 次）
- `[1, 1, 9, "bicubic", "center crop (square)", 8]`（1 次）
- `[1, 1, 1, "nearest", "keep aspect ratio", 8]`（1 次）
- `[1, 1, 9, "bicubic", "autocrop with mask", 16]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
