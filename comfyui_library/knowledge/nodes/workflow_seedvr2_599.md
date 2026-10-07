# workflow>SeedVR2 放大

## 节点类型

`workflow>SeedVR2 放大`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `blocks_to_swap:INT`（1 次）
- `use_non_blocking:BOOLEAN`（1 次）
- `offload_io_components:BOOLEAN`（1 次）
- `tiled_vae:BOOLEAN`（1 次）
- `vae_tile_size:INT`（1 次）
- `vae_tile_overlap:INT`（1 次）
- `preserve_vram:BOOLEAN`（1 次）
- `cache_model:BOOLEAN`（1 次）
- `enable_debug:BOOLEAN`（1 次）

## 输出

- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[16, false, false, true, 512, 64, false, false, false, "seedvr2_ema_3b_fp8_e4m3fn.safetensors", 1880451245, "randomize",`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
