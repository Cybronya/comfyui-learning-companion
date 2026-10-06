# ImageColorMatch+

## 节点类型

`ImageColorMatch+`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（6 次）
- `reference:IMAGE`（6 次）
- `reference_mask:MASK`（6 次）
- `color_space:COMBO`（6 次）
- `factor:FLOAT`（6 次）
- `device:COMBO`（6 次）
- `batch_size:INT`（6 次）

## 输出

- `IMAGE:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["LUV", 0.5, "auto", 0]`（3 次）
- `["RGB", 0.5, "auto", 0]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
