# workflow>控制

## 节点类型

`workflow>控制`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 image:IMAGE`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 mask:MASK`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 2 image:IMAGE`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 2 mask:MASK`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 3 image:IMAGE`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 3 mask:MASK`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）

## 输出

- `mask:MASK`（1 次）
- `original_size:BOX`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 mask:MASK`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 original_size:BOX`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 width:INT`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 height:INT`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 22 mask:MASK`（1 次）
- `LayerUtility: ImageScaleByAspectRatio V2 22 original_size:BOX`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[358834182040284, null, 778665641509943, null, 646474120492318, null, 964925692685729, "", "qwen_2.5_vl_7b_fp8_scaled.sa`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
