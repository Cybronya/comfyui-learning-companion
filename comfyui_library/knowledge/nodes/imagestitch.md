# ImageStitch

## 节点类型

`ImageStitch`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image1:IMAGE`（6 次）
- `image2:IMAGE`（6 次）
- `direction:COMBO`（6 次）
- `match_image_size:BOOLEAN`（6 次）
- `spacing_width:INT`（6 次）
- `spacing_color:COMBO`（6 次）

## 输出

- `IMAGE:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["right", true, 20, "white"]`（2 次）
- `["left", true, 20, "white"]`（2 次）
- `["right", true, 16, "black"]`（1 次）
- `["right", true, 0, "white"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
