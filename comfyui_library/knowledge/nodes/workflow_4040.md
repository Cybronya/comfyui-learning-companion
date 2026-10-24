# workflow>衣服图

## 节点类型

`workflow>衣服图`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:COMBO`（1 次）
- `upload:IMAGEUPLOAD`（1 次）
- `upscale_method:COMBO`（1 次）
- `megapixels:FLOAT`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `ImageScaleToTotalPixels 图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["pasted/d48dc1c001680b04e2856a04c4bda60cfb98d968407f3a1b114ab45396f7f771.png", "image", "nearest-exact", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
