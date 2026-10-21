# Colored Image (mtb)

## 节点类型

`Colored Image (mtb)`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `foreground_image:IMAGE`（3 次）
- `foreground_mask:MASK`（3 次）
- `color:COLOR`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `invert:BOOLEAN`（3 次）
- `mask_opacity:FLOAT`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["#9ea1ff", 341, 512, false, 1]`（1 次）
- `["#9441e6", 341, 512, false, 1]`（1 次）
- `["#f9e78b", 341, 512, false, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
