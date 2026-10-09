# AILab_ImageCompare

## 节点类型

`AILab_ImageCompare`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image1:IMAGE`（2 次）
- `image2:IMAGE`（2 次）
- `image3:IMAGE`（2 次）
- `text1:STRING`（2 次）
- `text2:STRING`（2 次）
- `text3:STRING`（2 次）
- `size_base:COMBO`（2 次）
- `text_color:COLORCODE`（2 次）
- `bg_color:COLORCODE`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["INPUT", "OUTPUT", "Image 3", "largest", "#000000", "#FFFFFF"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
