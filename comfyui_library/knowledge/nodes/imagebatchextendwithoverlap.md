# ImageBatchExtendWithOverlap

## 节点类型

`ImageBatchExtendWithOverlap`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `source_images:IMAGE`（4 次）
- `new_images:IMAGE`（4 次）
- `overlap:INT`（4 次）
- `overlap_side:COMBO`（4 次）
- `overlap_mode:COMBO`（4 次）

## 输出

- `source_images:IMAGE`（4 次）
- `start_images:IMAGE`（4 次）
- `extended_images:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[13, "new_images", "cut"]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
