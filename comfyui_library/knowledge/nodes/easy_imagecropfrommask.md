# easy imageCropFromMask

## 节点类型

`easy imageCropFromMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `image_crop_multi:FLOAT`（1 次）
- `mask_crop_multi:FLOAT`（1 次）
- `bbox_smooth_alpha:FLOAT`（1 次）

## 输出

- `crop_image:IMAGE`（1 次）
- `crop_mask:MASK`（1 次）
- `bbox:BBOX`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1.1500000000000004, 1.0000000000000002, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
