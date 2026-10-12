# PDImageResizeV3

## 节点类型

`PDImageResizeV3`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pixels:IMAGE`（1 次）
- `mask_optional:MASK`（1 次）
- `resize_mode:COMBO`（1 次）
- `target_size:INT`（1 次）
- `crop_mode:COMBO`（1 次）
- `target_width:INT`（1 次）
- `target_height:INT`（1 次）
- `horizontal_align:COMBO`（1 次）
- `vertical_align:COMBO`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `MASK:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["longest", 1280, "crop", 1280, 720, "center", "center"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
