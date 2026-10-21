# AILab_ImageResize

## 节点类型

`AILab_ImageResize`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `mask:MASK`（4 次）
- `custom_width:INT`（4 次）
- `custom_height:INT`（4 次）
- `megapixels:FLOAT`（4 次）
- `scale_by:FLOAT`（4 次）
- `resize_mode:COMBO`（4 次）
- `resize_value:INT`（4 次）
- `upscale_method:COMBO`（4 次）
- `device:COMBO`（4 次）

## 输出

- `IMAGE:IMAGE`（4 次）
- `MASK:MASK`（4 次）
- `WIDTH:INT`（4 次）
- `HEIGHT:INT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 1.5, 1, "longest_side", 0, "lanczos", "cpu", 64, "stretch", "center", "#FFFFFF"]`（2 次）
- `[512, 512, 0, 1, "longest_side", 1920, "nearest-exact", "cpu", 2, "crop", "center", "#FFFFFF"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
