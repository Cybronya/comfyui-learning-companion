# LayerUtility: ImageAutoCrop

## 节点类型

`LayerUtility: ImageAutoCrop`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `background_color:STRING`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `proportional_width:INT`（1 次）
- `proportional_height:INT`（1 次）
- `scale_to_longest_side:BOOLEAN`（1 次）
- `longest_side:INT`（1 次）
- `detect:COMBO`（1 次）
- `border_reserve:INT`（1 次）
- `ultra_detail_range:INT`（1 次）

## 输出

- `cropped_image:IMAGE`（1 次）
- `box_preview:IMAGE`（1 次）
- `cropped_mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["#FFFFFF", "custom", 2, 1, true, 1024, "min_bounding_rect", 100, 0, "RMBG 1.4", "sam_vit_h (2.56GB)", "GroundingDINO_Sw`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
