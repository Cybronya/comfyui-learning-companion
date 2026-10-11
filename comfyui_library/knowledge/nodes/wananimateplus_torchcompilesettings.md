# WanAnimatePlus TorchCompileSettings

## 节点类型

`WanAnimatePlus TorchCompileSettings`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `backend:COMBO`（1 次）
- `fullgraph:BOOLEAN`（1 次）
- `mode:COMBO`（1 次）
- `dynamic:BOOLEAN`（1 次）
- `dynamo_cache_size_limit:INT`（1 次）
- `compile_transformer_blocks_only:BOOLEAN`（1 次）
- `dynamo_recompile_limit:INT`（1 次）
- `force_parameter_static_shapes:BOOLEAN`（1 次）
- `allow_unmerged_lora_compile:BOOLEAN`（1 次）

## 输出

- `torch_compile_args:WANCOMPILEARGS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["inductor", false, "default", false, 64, true, 128, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
