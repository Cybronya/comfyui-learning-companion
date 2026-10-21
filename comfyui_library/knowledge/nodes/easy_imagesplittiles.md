# easy imageSplitTiles

## 节点类型

`easy imageSplitTiles`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `overlap_ratio:FLOAT`（1 次）
- `overlap_offset:INT`（1 次）
- `tiles_rows:INT`（1 次）
- `tiles_cols:INT`（1 次）
- `norm:BOOLEAN`（1 次）

## 输出

- `tiles:IMAGE`（1 次）
- `masks:MASK`（1 次）
- `overlap:OVERLAP`（1 次）
- `total:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.05, 0, 3, 3, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
