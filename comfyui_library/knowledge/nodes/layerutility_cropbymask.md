# LayerUtility: CropByMask

## 节点类型

`LayerUtility: CropByMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask_for_crop:MASK`（1 次）
- `invert_mask:BOOLEAN`（1 次）
- `detect:COMBO`（1 次）
- `top_reserve:INT`（1 次）
- `bottom_reserve:INT`（1 次）
- `left_reserve:INT`（1 次）
- `right_reserve:INT`（1 次）

## 输出

- `croped_image:IMAGE`（1 次）
- `croped_mask:MASK`（1 次）
- `crop_box:BOX`（1 次）
- `box_preview:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, "mask_area", 96, 96, 96, 96]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
