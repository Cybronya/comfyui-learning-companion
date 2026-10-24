# ImageBlendV1

## 节点类型

`ImageBlendV1`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `background_image:IMAGE`（3 次）
- `layer_image:IMAGE`（3 次）
- `layer_mask:MASK`（3 次）
- `blend_mode:COMBO`（3 次）
- `opacity:INT`（3 次）
- `x_percent:FLOAT`（3 次）
- `y_percent:FLOAT`（3 次）
- `scale:FLOAT`（3 次）
- `align_mode:COMBO`（3 次）
- `invert_mask:BOOLEAN`（3 次）

## 输出

- `image:IMAGE`（3 次）
- `mask:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["normal", 100, 50, 50, 1, "default", false]`（2 次）
- `["normal", 100, 50, 50, 1, "default", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
