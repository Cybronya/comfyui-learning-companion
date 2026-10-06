# QwenImage21BlockCacheT8

## 节点类型

`QwenImage21BlockCacheT8`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 28 个 workflow 中。

## 输入

- `model:MODEL`（28 次）
- `residual_diff_threshold:FLOAT`（28 次）
- `start_percent:FLOAT`（28 次）
- `end_percent:FLOAT`（28 次）
- `max_consecutive_hits:INT`（28 次）
- `cache_device:COMBO`（28 次）
- `metric_stride:INT`（28 次）
- `max_cache_mb:INT`（28 次）
- `threshold_mode:COMBO`（28 次）
- `split_ratio:FLOAT`（28 次）

## 输出

- `MODEL:MODEL`（28 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.08, 0.1, 0.85, 2, "cpu", 8, 1024, "constant", 0.5, 0.03]`（17 次）
- `[0.03, 0.1, 0.9, 2, "cpu", 8, 1024, "constant", 0.3500000000000001, 0.15000000000000002]`（11 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
