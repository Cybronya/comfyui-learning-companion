# YCImageAccumulator

## 节点类型

`YCImageAccumulator`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `selected_index:INT`（3 次）
- `clear_gallery:BOOLEAN`（3 次）
- `max_images:INT`（3 次）
- `update_position:INT`（3 次）
- `batch_start:INT`（3 次）
- `batch_end:INT`（3 次）
- `align_mode:COMBO`（3 次）
- `pad_color:STRING`（3 次）
- `save_to_output:BOOLEAN`（3 次）

## 输出

- `images:IMAGE`（3 次）
- `masks:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[-1, false, 9, -1, -1, -1, "largest", "#000000", false]`（2 次）
- `[-1, true, 9, -1, -1, -1, "largest", "#000000", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
