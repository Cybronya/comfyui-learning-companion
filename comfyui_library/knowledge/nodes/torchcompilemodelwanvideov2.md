# TorchCompileModelWanVideoV2

## 节点类型

`TorchCompileModelWanVideoV2`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `backend:COMBO`（1 次）
- `fullgraph:BOOLEAN`（1 次）
- `mode:COMBO`（1 次）
- `dynamic:BOOLEAN`（1 次）
- `compile_transformer_blocks_only:BOOLEAN`（1 次）
- `dynamo_cache_size_limit:INT`（1 次）

## 输出

- `MODEL:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["inductor", false, "default", false, true, 64]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
