# MiniMaxH3BlockCacheT8

## 节点类型

`MiniMaxH3BlockCacheT8`

## 分类

Optimization

## 作用

缓存/优化类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `model:MODEL`（9 次）
- `residual_diff_threshold:FLOAT`（9 次）
- `start_percent:FLOAT`（9 次）
- `end_percent:FLOAT`（9 次）
- `max_consecutive_hits:INT`（9 次）
- `cache_device:COMBO`（9 次）
- `metric_stride:INT`（9 次）
- `verbose:BOOLEAN`（9 次）

## 输出

- `MODEL:MODEL`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.14, 0.15000000000000002, 0.9000000000000001, 2, "cpu", 8, false]`（8 次）
- `[0.12, 0.08, 0.95, 2, "cpu", 8, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
