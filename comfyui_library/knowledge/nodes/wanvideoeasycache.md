# WanVideoEasyCache

## 节点类型

`WanVideoEasyCache`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `easycache_thresh:FLOAT`（2 次）
- `start_step:INT`（2 次）
- `end_step:INT`（2 次）
- `cache_device:COMBO`（2 次）

## 输出

- `cache_args:CACHEARGS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.015, 3, -1, "offload_device"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
