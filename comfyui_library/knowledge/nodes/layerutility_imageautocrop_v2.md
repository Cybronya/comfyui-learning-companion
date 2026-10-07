# LayerUtility: ImageAutoCrop V2

## 节点类型

`LayerUtility: ImageAutoCrop V2`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `fill_background:BOOLEAN`（1 次）
- `background_color:STRING`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `proportional_width:INT`（1 次）
- `proportional_height:INT`（1 次）
- `scale_to_side:COMBO`（1 次）
- `scale_to_length:INT`（1 次）
- `detect:COMBO`（1 次）

## 输出

- `cropped_image:IMAGE`（1 次）
- `box_preview:IMAGE`（1 次）
- `cropped_mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "#FFFFFF", "1:1", 1, 1, "longest", 1024, "min_bounding_rect", 50, 0, "SegmentAnything", "sam_vit_h (2.56GB)", "Gr`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
