# TTP_Image_Assy

## 节点类型

`TTP_Image_Assy`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 27 个 workflow 中。

## 输入

- `tiles:IMAGE`（45 次）
- `positions:LIST`（45 次）
- `original_size:TUPLE`（45 次）
- `grid_size:TUPLE`（45 次）
- `padding:INT`（45 次）

## 输出

- `RECONSTRUCTED_IMAGE:IMAGE`（45 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[64]`（24 次）
- `[128]`（20 次）
- `[256]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
