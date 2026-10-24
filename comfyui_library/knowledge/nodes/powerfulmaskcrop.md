# PowerfulMaskCrop

## 节点类型

`PowerfulMaskCrop`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `top_padding:INT`（2 次）
- `bottom_padding:INT`（2 次）
- `left_padding:INT`（2 次）
- `right_padding:INT`（2 次）
- `enable_resize:BOOLEAN`（2 次）
- `target_width:INT`（2 次）
- `target_height:INT`（2 次）
- `padding_mode:COMBO`（2 次）

## 输出

- `cropped_image:IMAGE`（2 次）
- `cropped_mask:MASK`（2 次）
- `crop_region_mask:MASK`（2 次）
- `crop_info:CROP_INFO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[100, 100, 60, 60, true, 0, 1280, "none", 16]`（1 次）
- `[30, 30, 30, 30, true, 0, 1280, "black", 16]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
