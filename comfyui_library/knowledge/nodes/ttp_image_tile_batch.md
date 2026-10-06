# TTP_Image_Tile_Batch

## 节点类型

`TTP_Image_Tile_Batch`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 27 个 workflow 中。

## 输入

- `image:IMAGE`（45 次）
- `tile_width:INT`（45 次）
- `tile_height:INT`（45 次）

## 输出

- `IMAGES:IMAGE`（45 次）
- `POSITIONS:LIST`（45 次）
- `ORIGINAL_SIZE:TUPLE`（45 次）
- `GRID_SIZE:TUPLE`（45 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 1024]`（36 次）
- `[1024, 787]`（5 次）
- `[["1030", 0], ["1030", 1]]`（2 次）
- `[["11", 0], ["11", 1]]`（1 次）
- `[2048, 2048]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
