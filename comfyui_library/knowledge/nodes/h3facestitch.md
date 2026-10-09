# H3FaceStitch

## 节点类型

`H3FaceStitch`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `base_images:IMAGE`（3 次）
- `refined_crops:IMAGE`（3 次）
- `transform:H3FACEXFORM`（3 次）
- `masks:MASK`（3 次）
- `paste_region:COMBO`（3 次）
- `mask_dilation:INT`（3 次）
- `feather:INT`（3 次）
- `colour_match:FLOAT`（3 次）
- `blend:FLOAT`（3 次）
- `undetected_frames:COMBO`（3 次）

## 输出

- `images:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["face_only", 24, 24, 1, 1, "fade_out", false]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
