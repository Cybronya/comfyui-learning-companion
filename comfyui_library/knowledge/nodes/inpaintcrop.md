# InpaintCrop

## 节点类型

`InpaintCrop`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `mask:MASK`（3 次）
- `optional_context_mask:MASK`（3 次）
- `context_expand_pixels:INT`（3 次）
- `context_expand_factor:FLOAT`（3 次）
- `fill_mask_holes:BOOLEAN`（3 次）
- `blur_mask_pixels:FLOAT`（3 次）
- `invert_mask:BOOLEAN`（3 次）
- `blend_pixels:FLOAT`（3 次）
- `rescale_algorithm:COMBO`（3 次）

## 输出

- `stitch:STITCH`（3 次）
- `cropped_image:IMAGE`（3 次）
- `cropped_mask:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[21, 1, true, 17, false, 16, "lanczos", "ranged size", 1024, 1024, 1, 512, 512, 768, 768, 32]`（2 次）
- `[50, 1, true, 16, false, 16, "bicubic", "forced size", 2048, 2048, 1, 512, 512, 768, 768, 32]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
