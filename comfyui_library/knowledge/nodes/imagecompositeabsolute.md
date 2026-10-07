# ImageCompositeAbsolute

## 节点类型

`ImageCompositeAbsolute`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images_a:IMAGE`（6 次）
- `images_b:IMAGE`（6 次）
- `images_a_x:INT`（6 次）
- `images_a_y:INT`（6 次）
- `images_b_x:INT`（6 次）
- `images_b_y:INT`（6 次）
- `container_width:INT`（6 次）
- `container_height:INT`（6 次）
- `background:COMBO`（6 次）
- `method:COMBO`（6 次）

## 输出

- `IMAGE:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 0, 0, 0, 0, "images_a", "pair"]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
