# SeedVR2TorchCompileSettings

## 节点类型

`SeedVR2TorchCompileSettings`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `backend:COMBO`（3 次）
- `mode:COMBO`（3 次）
- `fullgraph:BOOLEAN`（3 次）
- `dynamic:BOOLEAN`（3 次）
- `dynamo_cache_size_limit:INT`（3 次）
- `dynamo_recompile_limit:INT`（3 次）

## 输出

- `torch_compile_args:SEEDVR2_TORCH_COMPILE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["inductor", "default", false, false, 64, 128]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
