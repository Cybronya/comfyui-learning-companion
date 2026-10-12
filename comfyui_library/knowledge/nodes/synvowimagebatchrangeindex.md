# SynVowImageBatchRangeIndex

## 节点类型

`SynVowImageBatchRangeIndex`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（3 次）
- `batch_size:INT`（3 次）
- `group_index:INT`（3 次）

## 输出

- `images:IMAGE`（3 次）
- `range_frame:STRING`（3 次）
- `all_ranges:STRING`（3 次）
- `total_groups:FLOAT,INT,NUMBER,STRING`（3 次）
- `current_group_frames:FLOAT,INT,NUMBER,STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[81, 0]`（2 次）
- `[1, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
