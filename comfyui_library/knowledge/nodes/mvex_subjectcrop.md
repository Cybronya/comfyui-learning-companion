# MVEx_SubjectCrop

## 节点类型

`MVEx_SubjectCrop`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `original_images:IMAGE`（8 次）
- `masks:MASK`（8 次）
- `mode:COMFY_DYNAMICCOMBO_V3`（8 次）
- `mode.crop_scale:FLOAT`（8 次）
- `mode.padding:COMBO`（8 次）
- `mode.prefer:COMBO`（8 次）
- `mode.aspect_ratio:FLOAT`（8 次）
- `mode.seamless_loop:BOOLEAN`（8 次）
- `divisible_by:INT`（8 次）
- `upscale_megapixels:FLOAT`（8 次）

## 输出

- `cropped_images:IMAGE`（8 次）
- `cropped_masks:MASK`（8 次）
- `bboxes:BOUNDING_BOX`（8 次）
- `debug:STRING`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["tracked", 1.7500000000000004, "firm", "stillness", 0, false, 32, 0, "auto"]`（8 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
