# ImageTile+

## 节点类型

`ImageTile+`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `rows:INT`（1 次）
- `cols:INT`（1 次）
- `overlap:FLOAT`（1 次）
- `overlap_x:INT`（1 次）
- `overlap_y:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `tile_width:INT`（1 次）
- `tile_height:INT`（1 次）
- `overlap_x:INT`（1 次）
- `overlap_y:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, 2, 0, 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
