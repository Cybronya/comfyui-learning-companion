# EasyCache

## 节点类型

`EasyCache`

## 分类

Optimization

## 作用

缓存/优化类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 14 个 workflow 中。

## 输入

- `model:MODEL`（17 次）
- `reuse_threshold:FLOAT`（17 次）
- `start_percent:FLOAT`（17 次）
- `end_percent:FLOAT`（17 次）
- `verbose:BOOLEAN`（17 次）

## 输出

- `MODEL:MODEL`（17 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.3, 0.35, 0.9, false]`（6 次）
- `[0.20000000000000004, 0.15000000000000002, 0.9000000000000001, false]`（5 次）
- `[0.2, 0.15, 0.95, false]`（4 次）
- `[0.30000000000000004, 0.20000000000000004, 0.9000000000000001, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
