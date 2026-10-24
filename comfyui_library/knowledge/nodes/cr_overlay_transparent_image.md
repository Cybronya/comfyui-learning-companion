# CR Overlay Transparent Image

## 节点类型

`CR Overlay Transparent Image`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `back_image:IMAGE`（11 次）
- `overlay_image:IMAGE`（11 次）
- `transparency:FLOAT`（6 次）
- `offset_x:INT`（6 次）
- `offset_y:INT`（6 次）
- `rotation_angle:FLOAT`（6 次）
- `overlay_scale_factor:FLOAT`（6 次）

## 输出

- `IMAGE:IMAGE`（11 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 0, 0, 1]`（7 次）
- `[1, 0, 0, 0, 1]`（3 次）
- `[0, 0, -400, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
