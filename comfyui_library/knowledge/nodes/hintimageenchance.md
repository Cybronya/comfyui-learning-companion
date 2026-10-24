# HintImageEnchance

## 节点类型

`HintImageEnchance`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `hint_image:IMAGE`（2 次）
- `image_gen_width:INT`（1 次）
- `image_gen_height:INT`（1 次）
- `resize_mode:COMBO`（1 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[768, 1024, "Crop and Resize"]`（1 次）
- `[2048, 2800, "Resize and Fill"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
