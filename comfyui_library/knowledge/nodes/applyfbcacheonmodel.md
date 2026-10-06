# ApplyFBCacheOnModel

## 节点类型

`ApplyFBCacheOnModel`

## 分类

Optimization

## 作用

缓存/优化类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `model:MODEL`（5 次）
- `object_to_patch:STRING`（1 次）
- `residual_diff_threshold:FLOAT`（1 次）
- `start:FLOAT`（1 次）
- `end:FLOAT`（1 次）
- `max_consecutive_cache_hits:INT`（1 次）

## 输出

- `MODEL:MODEL`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["diffusion_model", 0.12, 0, 1, -1]`（4 次）
- `["diffusion_model", 0.07, 0, 1, -1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
