# RembgByBiRefNetAdvanced

## 节点类型

`RembgByBiRefNetAdvanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:BIREFNET`（1 次）
- `images:IMAGE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `upscale_method:COMBO`（1 次）
- `blur_size:INT`（1 次）
- `blur_size_two:INT`（1 次）
- `fill_color:BOOLEAN`（1 次）
- `color:INT`（1 次）
- `mask_threshold:FLOAT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1280, 1280, "bicubic", 201, 21, true, 13882323, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
