# ImageTransformKJ

## 节点类型

`ImageTransformKJ`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE,MASK`（1 次）
- `mask:MASK`（1 次）
- `target_width:INT`（1 次）
- `target_height:INT`（1 次）
- `upscale_method:COMBO`（1 次）
- `keep_proportion:COMFY_DYNAMICCOMBO_V3`（1 次）
- `divisible_by:INT`（1 次）
- `extra_padding:COMFY_DYNAMICCOMBO_V3`（1 次）
- `invert_crop:COMFY_DYNAMICCOMBO_V3`（1 次）
- `bboxes:STRING`（1 次）

## 输出

- `output:*`（1 次）
- `output_mask:MASK`（1 次）
- `bbox:BBOX`（1 次）
- `bbox_mask:MASK`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, "lanczos", "keep_long_edge", 2, "disabled", "disabled", "{\"fillColor\":\"#000000\",\"bboxes\":[{\"startX\":45.50`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
