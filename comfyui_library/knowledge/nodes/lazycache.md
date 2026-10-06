# LazyCache

## 节点类型

`LazyCache`

## 分类

Optimization

## 作用

缓存/优化类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `reuse_threshold:FLOAT`（2 次）
- `start_percent:FLOAT`（2 次）
- `end_percent:FLOAT`（2 次）
- `verbose:BOOLEAN`（2 次）

## 输出

- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.12000000000000002, 0.25000000000000006, 0.7500000000000001, false]`（1 次）
- `[0.2, 0.15, 0.95, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
