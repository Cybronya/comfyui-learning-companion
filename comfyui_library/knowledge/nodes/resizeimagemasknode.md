# ResizeImageMaskNode

## 节点类型

`ResizeImageMaskNode`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 14 个 workflow 中。

## 输入

- `input:IMAGE,MASK`（15 次）
- `resize_type:COMFY_DYNAMICCOMBO_V3`（15 次）
- `scale_method:COMBO`（15 次）
- `resize_type.multiplier:FLOAT`（7 次）
- `resize_type.megapixels:FLOAT`（6 次）
- `resize_type.multiple:INT`（1 次）
- `resize_type.height:INT`（1 次）

## 输出

- `resized:*`（15 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["scale total pixels", 16, "bilinear"]`（6 次）
- `["scale by multiplier", 1, "lanczos"]`（6 次）
- `["scale to multiple", "area", 8]`（1 次）
- `["scale by multiplier", "area", 1]`（1 次）
- `["scale height", 2048, "area"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
