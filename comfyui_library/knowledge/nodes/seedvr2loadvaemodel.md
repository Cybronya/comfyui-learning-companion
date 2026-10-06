# SeedVR2LoadVAEModel

## 节点类型

`SeedVR2LoadVAEModel`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 67 个 workflow 中。

## 输入

- `cache_model:MODEL`（71 次）
- `torch_compile_args:SEEDVR2_TORCH_COMPILE`（71 次）
- `model:COMBO`（71 次）
- `device:COMBO`（71 次）
- `encode_tiled:BOOLEAN`（71 次）
- `encode_tile_size:INT`（71 次）
- `encode_tile_overlap:INT`（71 次）
- `decode_tiled:BOOLEAN`（71 次）
- `decode_tile_size:INT`（71 次）
- `decode_tile_overlap:INT`（71 次）

## 输出

- `vae:SEEDVR2_VAE`（71 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ema_vae_fp16.safetensors", "cuda:0", true, 1024, 128, true, 1024, 128, "false", "cpu"]`（15 次）
- `["ema_vae_fp16.safetensors", "cuda:0", true, 512, 64, true, 512, 64, "false", "cpu"]`（14 次）
- `["ema_vae_fp16.safetensors", "cuda:0", false, 256, 32, false, 256, 32, "false", "none"]`（10 次）
- `["ema_vae_fp16.safetensors", "cuda:0", false, 256, 32, false, 256, 32, "false", "cpu"]`（10 次）
- `["ema_vae_fp16.safetensors", "cuda:0", false, 1024, 128, true, 1024, 128, "false", "none"]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
