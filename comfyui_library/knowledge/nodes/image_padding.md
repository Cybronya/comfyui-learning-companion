# Image Padding

## 节点类型

`Image Padding`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 33 个 workflow 中。

## 输入

- `image:IMAGE`（33 次）
- `feathering:INT`（13 次）
- `feather_second_pass:COMBO`（13 次）
- `left_padding:INT`（13 次）
- `right_padding:INT`（13 次）
- `top_padding:INT`（13 次）
- `bottom_padding:INT`（13 次）

## 输出

- `IMAGE:IMAGE`（33 次）
- `MASK:IMAGE`（33 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[120, "true", 512, 512, 512, 512]`（21 次）
- `[120, "true", 256, 256, 1024, 256]`（7 次）
- `[0, "true", 8, 8, 8, 8]`（3 次）
- `[50, "true", 100, 100, 100, 100]`（1 次）
- `[0, "false", 8, 8, 600, 8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
