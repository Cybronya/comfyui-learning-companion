# Image Crop Location

## 节点类型

`Image Crop Location`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `right:INT`（4 次）
- `left:INT`（4 次）
- `bottom:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（4 次）
- `CROP_DATA:CROP_DATA`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 1024, 2048, 1024]`（3 次）
- `[0, 1024, 2048, 768]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
