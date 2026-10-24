# PixelSnapping

## 节点类型

`PixelSnapping`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `reference_image:IMAGE`（4 次）
- `target_image:IMAGE`（4 次）
- `target_mask:MASK`（4 次）
- `max_features:INT`（4 次）
- `match_ratio:FLOAT`（4 次）
- `ransac_threshold:FLOAT`（4 次）
- `invert_input_mask:BOOLEAN`（4 次）
- `mask_grow:INT`（4 次）
- `mask_blur:FLOAT`（4 次）
- `invert_output_mask:BOOLEAN`（4 次）

## 输出

- `stitched_image:IMAGE`（4 次）
- `mask:MASK`（4 次）
- `corrected_target:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[5000, 0.75, 5, false, 0, 0, false]`（3 次）
- `[5000, 0.75, 5, false, -35, 10, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
