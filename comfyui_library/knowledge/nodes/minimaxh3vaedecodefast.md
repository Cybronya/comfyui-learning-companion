# MiniMaxH3VAEDecodeFast

## 节点类型

`MiniMaxH3VAEDecodeFast`

## 分类

Decoding

## 作用

解码类节点：把编码数据还原（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `samples:LATENT`（7 次）
- `vae:VAE`（7 次）
- `tiling:BOOLEAN`（7 次）
- `tile_size:INT`（7 次）
- `tile_overlap:INT`（7 次）
- `output_device:COMBO`（7 次）
- `temporal_tiling:BOOLEAN`（7 次）
- `temporal_tile_frames:INT`（7 次）
- `temporal_context_frames:INT`（7 次）
- `seam_warning_threshold:FLOAT`（7 次）

## 输出

- `images:IMAGE`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 256, 64, "cpu", false, 85, 39, 0.02]`（7 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
