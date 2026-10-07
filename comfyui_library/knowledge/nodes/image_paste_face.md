# Image Paste Face

## 节点类型

`Image Paste Face`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `crop_image:IMAGE`（1 次）
- `crop_data:CROP_DATA`（1 次）
- `crop_blending:FLOAT`（1 次）
- `crop_sharpening:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `MASK_IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.25, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
