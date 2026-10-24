# Image Transpose

## 节点类型

`Image Transpose`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `image_overlay:IMAGE`（3 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `X:INT`（2 次）
- `Y:INT`（2 次）
- `rotation:INT`（1 次）
- `feathering:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, 0, 0, 0, 0]`（2 次）
- `[576, 768, 0, 0, 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
