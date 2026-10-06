# SeedVR2

## 节点类型

`SeedVR2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `images:IMAGE`（4 次）
- `block_swap_config:block_swap_config`（4 次）
- `extra_args:extra_args`（4 次）
- `model:COMBO`（4 次）
- `seed:INT`（4 次）
- `new_resolution:INT`（4 次）
- `batch_size:INT`（4 次）

## 输出

- `image:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["seedvr2_ema_7b_fp16.safetensors", 1865931904, "randomize", 2048, 5]`（2 次）
- `["seedvr2_ema_3b_fp8_e4m3fn.safetensors", 100, "fixed", 2048, 1]`（1 次）
- `["seedvr2_ema_7b_fp16.safetensors", 1731321847, "randomize", 2048, 5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
