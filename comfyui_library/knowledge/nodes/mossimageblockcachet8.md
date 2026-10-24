# MOSSImageBlockCacheT8

## 节点类型

`MOSSImageBlockCacheT8`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `enabled:BOOLEAN`（2 次）
- `threshold:FLOAT`（2 次）
- `start_percent:FLOAT`（2 次）
- `end_percent:FLOAT`（2 次）
- `max_consecutive_hits:INT`（2 次）
- `cache_device:COMBO`（2 次）
- `max_cache_mb:INT`（2 次）
- `metric_stride:INT`（2 次）
- `threshold_mode:COMBO`（2 次）

## 输出

- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 0.08000000000000002, 0.1, 0.9, 1, "gpu", 512, 4, "constant", 0.30000000000000004, 0.14000000000000004]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
