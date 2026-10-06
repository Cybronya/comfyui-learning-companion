# SeedVR2GGUF

## 节点类型

`SeedVR2GGUF`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images:IMAGE`（2 次）
- `block_swap_config:block_swap_config`（2 次）
- `extra_args:extra_args`（2 次）
- `model:COMBO`（2 次）
- `seed:INT`（2 次）
- `new_resolution:INT`（2 次）
- `batch_size:INT`（2 次）

## 输出

- `image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["seedvr2_ema_7b-Q3_K_M.gguf", 139099305, "randomize", 1072, 5]`（1 次）
- `["seedvr2_ema_3b-Q8_0.gguf", 666666, "fixed", 4096, 41]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
