# BatchCropFromMaskAdvanced

## 节点类型

`BatchCropFromMaskAdvanced`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `original_images:IMAGE`（7 次）
- `masks:MASK`（7 次）
- `crop_size_mult:FLOAT`（7 次）
- `bbox_smooth_alpha:FLOAT`（7 次）

## 输出

- `original_images:IMAGE`（7 次）
- `cropped_images:IMAGE`（7 次）
- `cropped_masks:MASK`（7 次）
- `combined_crop_image:IMAGE`（7 次）
- `combined_crop_masks:MASK`（7 次）
- `bboxes:BBOX`（7 次）
- `combined_bounding_box:BBOX`（7 次）
- `bbox_width:INT`（7 次）
- `bbox_height:INT`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1.5, 0.5]`（3 次）
- `[4, 0.5]`（2 次）
- `[1, 0.5]`（1 次）
- `[1.0000000000000002, 0.5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
