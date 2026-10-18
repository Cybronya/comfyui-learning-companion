# MiniMaxH3QwenReferencePrefixCacheT8Advanced

## 节点类型

`MiniMaxH3QwenReferencePrefixCacheT8Advanced`

## 分类

Optimization

## 作用

缓存/优化类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）
- `mode:COMBO`（2 次）
- `max_entries:INT`（2 次）
- `maximum_cache_mib:FLOAT`（2 次）
- `cache_epoch:INT`（2 次）

## 输出

- `clip:CLIP`（2 次）
- `cache_handle:H3_T8_QWEN_PREFIX_CACHE`（2 次）
- `report_json:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["memory_lru_exp", 1, 1024, 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
