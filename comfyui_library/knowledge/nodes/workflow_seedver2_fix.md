# workflow>seedver2 fix

## 节点类型

`workflow>seedver2 fix`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `*:*`（4 次）
- `image:IMAGE`（4 次）
- `blocks_to_swap:INT`（4 次）
- `use_non_blocking:BOOLEAN`（4 次）
- `offload_io_components:BOOLEAN`（4 次）
- `tiled_vae:BOOLEAN`（4 次）
- `vae_tile_size:INT`（4 次）
- `vae_tile_overlap:INT`（4 次）
- `preserve_vram:BOOLEAN`（4 次）
- `cache_model:BOOLEAN`（4 次）

## 输出

- `*:*`（4 次）
- `image_urls:STRING`（4 次）
- `SaveImage image_urls:STRING`（4 次）
- `PlaySound|pysssss *:*`（4 次）
- `Reroute *:*`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[16, true, false, true, 512, 64, true, true, true, "lanczos", 0.30000000000000004, 1, "seedvr2_ema_3b_fp8_e4m3fn.safeten`（3 次）
- `[16, true, false, true, 512, 64, true, true, true, "lanczos", 0.30000000000000004, 1, "seedvr2_ema_3b_fp8_e4m3fn.safeten`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
