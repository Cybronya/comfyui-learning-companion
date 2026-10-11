# HyVideoDecode

## 节点类型

`HyVideoDecode`

## 分类

Decoding

## 作用

解码类节点：把编码数据还原（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vae:VAE`（1 次）
- `samples:LATENT`（1 次）
- `enable_vae_tiling:BOOLEAN`（1 次）
- `temporal_tiling_sample_size:INT`（1 次）
- `spatial_tile_sample_min_size:INT`（1 次）
- `auto_tile_size:BOOLEAN`（1 次）
- `skip_latents:INT`（1 次）
- `balance_brightness:BOOLEAN`（1 次）

## 输出

- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 16, 128, true, 0, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
