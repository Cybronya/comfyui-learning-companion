# CompositeImages_

## 节点类型

`CompositeImages_`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `foreground:*`（3 次）
- `mask:MASK`（3 次）
- `background:IMAGE`（3 次）
- `is_multiply_blend:BOOLEAN`（3 次）
- `position:COMBO`（3 次）
- `scale:FLOAT`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "center_center", 1]`（2 次）
- `[false, "center_center", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
