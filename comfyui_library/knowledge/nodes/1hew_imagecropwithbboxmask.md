# 1hew_ImageCropWithBBoxMask

## 节点类型

`1hew_ImageCropWithBBoxMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `get_crop_ratio:IMAGE`（1 次）
- `preset_ratio:COMBO`（1 次）
- `scale_strength:FLOAT`（1 次）
- `crop_to_side:COMBO`（1 次）
- `crop_to_length:INT`（1 次）
- `divisible_by:INT`（1 次）

## 输出

- `cropped_image:IMAGE`（1 次）
- `bbox_mask:MASK`（1 次）
- `cropped_mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["mask", 0, "None", 1028, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
