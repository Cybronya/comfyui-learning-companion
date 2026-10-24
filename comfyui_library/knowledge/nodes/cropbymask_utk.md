# CropByMask_UTK

## 节点类型

`CropByMask_UTK`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `image:IMAGE`（9 次）
- `mask_for_crop:MASK`（9 次）
- `invert_mask:BOOLEAN`（9 次）
- `detect:COMBO`（9 次）
- `top_reserve:INT`（9 次）
- `bottom_reserve:INT`（9 次）
- `left_reserve:INT`（9 次）
- `right_reserve:INT`（9 次）

## 输出

- `croped_image:IMAGE`（9 次）
- `croped_mask:MASK`（9 次）
- `crop_box:BOX`（9 次）
- `box_preview:IMAGE`（9 次）
- `remaining_area:MASK`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, "min_bounding_rect", 20, 20, 20, 20]`（5 次）
- `[false, "mask_area", 150, 50, 100, 100]`（2 次）
- `[false, "min_bounding_rect", 100, 200, 200, 200]`（1 次）
- `[false, "mask_area", 0, 0, 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
