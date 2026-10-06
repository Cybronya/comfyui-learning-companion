# TTP_Tile_image_size

## 节点类型

`TTP_Tile_image_size`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 26 个 workflow 中。

## 输入

- `image:IMAGE`（44 次）
- `width_factor:INT`（44 次）
- `height_factor:INT`（44 次）
- `overlap_rate:FLOAT`（44 次）

## 输出

- `tile_width:INT`（44 次）
- `tile_height:INT`（44 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[3, 4, 0.1]`（12 次）
- `[3, 4, 0.15000000000000002]`（6 次）
- `[2, 2, 0.05]`（5 次）
- `[3, 3, 0.10000000000000002]`（5 次）
- `[2, 3, 0.05000000000000001]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
