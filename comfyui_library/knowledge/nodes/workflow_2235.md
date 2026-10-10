# workflow>加速节点

## 节点类型

`workflow>加速节点`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（6 次）
- `sage_attention:COMBO`（6 次）
- `enable_fp16_accumulation:BOOLEAN`（6 次）
- `backend:COMBO`（6 次）
- `fullgraph:BOOLEAN`（6 次）
- `mode:COMBO`（6 次）
- `dynamic:BOOLEAN`（6 次）
- `compile_transformer_blocks_only:BOOLEAN`（6 次）
- `dynamo_cache_size_limit:INT`（6 次）

## 输出

- `MODEL:MODEL`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto", true, "inductor", false, "default", false, true, 64]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
