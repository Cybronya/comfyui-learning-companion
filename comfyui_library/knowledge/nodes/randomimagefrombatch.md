# RandomImageFromBatch

## 节点类型

`RandomImageFromBatch`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `input:IMAGE,MASK`（2 次）
- `start_index:INT`（2 次）
- `end_index:INT`（2 次）
- `num_frames:INT`（2 次）
- `randomness:FLOAT`（2 次）
- `min_distance:INT`（2 次）
- `max_distance:INT`（2 次）
- `seed:INT`（2 次）

## 输出

- `output:*`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, -1, 124, 0, 0, 0, 71329596207821, "randomize"]`（1 次）
- `[0, -1, 7, 0, 0, 0, 572308569177830, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
