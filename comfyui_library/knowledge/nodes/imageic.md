# ImageIC

## 节点类型

`ImageIC`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `first_image:IMAGE`（2 次）
- `second_image:IMAGE`（2 次）
- `first_mask:MASK`（2 次）
- `second_mask:MASK`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `MASK:MASK`（2 次）
- `FIRST_MASK:MASK`（2 次）
- `SECOND_MASK:MASK`（2 次）
- `first_size:TUPLE`（2 次）
- `second_size:TUPLE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["image1_height", "horizontal", 1, "center", 1024, "#FFFFFF"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
