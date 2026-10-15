# kkImageSplit

## 节点类型

`kkImageSplit`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `grid_size:COMBO`（3 次）
- `custom_width:INT`（3 次）
- `custom_height:INT`（3 次）
- `overlap_pixels:INT`（3 次）
- `output_order:COMBO`（3 次）

## 输出

- `merged_tiles:IMAGE`（3 次）
- `tile_01:IMAGE`（3 次）
- `tile_02:IMAGE`（3 次）
- `tile_03:IMAGE`（3 次）
- `tile_04:IMAGE`（3 次）
- `tile_05:IMAGE`（3 次）
- `tile_06:IMAGE`（3 次）
- `tile_07:IMAGE`（3 次）
- `tile_08:IMAGE`（3 次）
- `tile_09:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["2x2", 2, 2, 0, "row-major"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
