# GetImageRangeFromBatch

## 节点类型

`GetImageRangeFromBatch`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `images:IMAGE`（26 次）
- `masks:MASK`（26 次）
- `start_index:INT`（26 次）
- `num_frames:INT`（26 次）

## 输出

- `IMAGE:IMAGE`（26 次）
- `MASK:MASK`（26 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 1]`（11 次）
- `[38, 1]`（10 次）
- `[0, 38]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
