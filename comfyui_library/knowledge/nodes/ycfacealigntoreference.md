# YCFaceAlignToReference

## 节点类型

`YCFaceAlignToReference`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `analysis_models:ANALYSIS_MODELS`（1 次）
- `reference_image:IMAGE`（1 次）
- `target_image:IMAGE`（1 次）
- `scale_mode:COMBO`（1 次）
- `reference_face_index:INT`（1 次）
- `target_face_index:INT`（1 次）
- `padding:INT`（1 次）
- `horizontal_offset:INT`（1 次）
- `vertical_offset:INT`（1 次）
- `background_color:STRING`（1 次）

## 输出

- `aligned_image:IMAGE`（1 次）
- `mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["keep_aspect_ratio", 0, 0, 0, 0, 0, "#000000"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
