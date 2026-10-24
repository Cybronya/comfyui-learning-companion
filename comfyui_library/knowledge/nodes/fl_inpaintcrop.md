# FL_InpaintCrop

## 节点类型

`FL_InpaintCrop`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `optional_context_mask:MASK`（1 次）
- `context_factor:FLOAT`（1 次）
- `target_size:INT`（1 次）
- `resize_mode:COMBO`（1 次）
- `force_square:BOOLEAN`（1 次）
- `divisible_by:INT`（1 次）
- `invert_mask:BOOLEAN`（1 次）
- `fill_mask_holes:BOOLEAN`（1 次）

## 输出

- `stitch:STITCH`（1 次）
- `cropped_image:IMAGE`（1 次）
- `cropped_mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1.2, 1024, "bucket", false, 8, false, true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
