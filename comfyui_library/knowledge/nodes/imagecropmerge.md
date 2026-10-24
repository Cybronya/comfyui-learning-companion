# ImageCropMerge

## 节点类型

`ImageCropMerge`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `cropped_image:IMAGE`（6 次）
- `original_image:IMAGE`（6 次）
- `crop_x:INT`（6 次）
- `crop_y:INT`（6 次）
- `cropped_original_width:INT`（6 次）
- `cropped_original_height:INT`（6 次）
- `resize_method:COMBO`（4 次）

## 输出

- `IMAGE:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["lanczos"]`（4 次）
- `[0, 0, 512, 512, "lanczos"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
