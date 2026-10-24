# RefineAnything_Pasteback

## 节点类型

`RefineAnything_Pasteback`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `generated_image:IMAGE`（1 次）
- `cond:CONDITIONING`（1 次）
- `mask_grow:INT`（1 次）
- `blend_blur:INT`（1 次）
- `adain:BOOLEAN`（1 次）
- `wavelet:BOOLEAN`（1 次）
- `save_rgba:BOOLEAN`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `transparent_bg:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[12, 3, true, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
