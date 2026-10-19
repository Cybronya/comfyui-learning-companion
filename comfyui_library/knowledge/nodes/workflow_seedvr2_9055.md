# workflow>seedvr2

## 节点类型

`workflow>seedvr2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `cache_model:MODEL`（1 次）
- `torch_compile_args:SEEDVR2_TORCH_COMPILE`（1 次）
- `image:IMAGE`（1 次）
- `dit:SEEDVR2_DIT`（1 次）
- `vae:SEEDVR2_VAE`（1 次）
- `SeedVR2LoadDiTModel cache_model:MODEL`（1 次）
- `SeedVR2LoadDiTModel torch_compile_args:SEEDVR2_TORCH_COMPILE`（1 次）
- `images:IMAGE`（1 次）
- `tile_debug:COMBO`（1 次）
- `offload_device:COMBO`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["false", "none", "ema_vae_fp16.safetensors", "cuda:0", false, 1024, 128, false, 1024, 128, 0, 0, 0, "cpu", false, 41076`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
