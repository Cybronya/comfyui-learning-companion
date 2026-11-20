# 1hew_ImageMaskBlend

## 节点类型

`1hew_ImageMaskBlend`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `fill_hole:BOOLEAN`（1 次）
- `invert:BOOLEAN`（1 次）
- `feather:INT`（1 次）
- `opacity:FLOAT`（1 次）
- `expansion:INT`（1 次）
- `background_color:STRING`（1 次）
- `background_opacity:FLOAT`（1 次）
- `output_mask_invert:BOOLEAN`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, false, 0, 1, 0, "0", 0.7000000000000002, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
