# InpaintCropImproved

## 节点类型

`InpaintCropImproved`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `mask:MASK`（4 次）
- `optional_context_mask:MASK`（4 次）
- `downscale_algorithm:COMBO`（4 次）
- `upscale_algorithm:COMBO`（4 次）
- `preresize:BOOLEAN`（4 次）
- `preresize_mode:COMBO`（4 次）
- `preresize_min_width:INT`（4 次）
- `preresize_min_height:INT`（4 次）
- `preresize_max_width:INT`（4 次）

## 输出

- `stitcher:STITCHER`（4 次）
- `cropped_image:IMAGE`（4 次）
- `cropped_mask:MASK`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["bilinear", "bicubic", false, "ensure minimum resolution", 1024, 1024, 16384, 16384, true, 50, false, 32, 0.1, false, 1`（2 次）
- `["lanczos", "lanczos", false, "ensure minimum resolution", 1024, 1024, 16384, 16384, true, 50, false, 32, 0.1, false, 1,`（1 次）
- `["bilinear", "bicubic", false, "ensure minimum resolution", 1024, 1024, 16384, 16384, true, 0, false, 32, 0.1, false, 1,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
