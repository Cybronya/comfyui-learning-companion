# DF_Image_scale_by_ratio

## 节点类型

`DF_Image_scale_by_ratio`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `upscale_by:FLOAT`（2 次）
- `upscale_method:COMBO`（2 次）
- `crop:COMBO`（2 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2.0000000000000004, "nearest-exact", "disabled"]`（1 次）
- `[1.5000000000000002, "bicubic", "disabled"]`（1 次）
- `[1, "nearest-exact", "disabled"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
