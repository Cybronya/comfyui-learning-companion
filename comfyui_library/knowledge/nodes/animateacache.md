# AnimaTeaCache

## 节点类型

`AnimaTeaCache`

## 分类

Optimization

## 作用

缓存/优化类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `threshold:FLOAT`（1 次）
- `teacache_version:COMBO`（1 次）
- `adaptive_mode:BOOLEAN`（1 次）
- `early_steps_factor:FLOAT`（1 次）
- `late_steps_factor:FLOAT`（1 次）
- `start_percent:FLOAT`（1 次）
- `end_percent:FLOAT`（1 次）
- `cache_device:COMBO`（1 次）

## 输出

- `model:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.15, "v2 (Standard Precise)", true, 0.4, 1.8, 0, 1, "cuda"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
