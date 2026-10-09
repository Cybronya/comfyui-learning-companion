# ImageColorMatchAdobe+

## 节点类型

`ImageColorMatchAdobe+`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `reference:IMAGE`（1 次）
- `reference_mask:MASK`（1 次）
- `color_space:COMBO`（1 次）
- `luminance_factor:FLOAT`（1 次）
- `color_intensity_factor:FLOAT`（1 次）
- `fade_factor:FLOAT`（1 次）
- `neutralization_factor:FLOAT`（1 次）
- `device:COMBO`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["RGB", 1, 1, 1, 0, "auto"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
