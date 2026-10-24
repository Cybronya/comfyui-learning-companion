# Trellis2LoadImageWithTransparency

## 节点类型

`Trellis2LoadImageWithTransparency`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:COMBO`（1 次）
- `upload:IMAGEUPLOAD`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `image_with_alpha:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["25dc498f83a943db582697ce6d5422aa0fce206432e58d418096348dc5196ae7.jpg", "image"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
