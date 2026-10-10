# LTXVSpatioTemporalTiledVAEDecode

## 节点类型

`LTXVSpatioTemporalTiledVAEDecode`

## 分类

Decoding

## 作用

解码类节点：把编码数据还原（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `vae:VAE`（5 次）
- `latents:LATENT`（5 次）
- `spatial_tiles:INT`（5 次）
- `spatial_overlap:INT`（5 次）
- `temporal_tile_length:INT`（5 次）
- `temporal_overlap:INT`（5 次）
- `last_frame_fix:BOOLEAN`（5 次）
- `working_device:COMBO`（5 次）
- `working_dtype:COMBO`（5 次）

## 输出

- `image:IMAGE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4, 4, 16, 4, false, "auto", "auto"]`（4 次）
- `[4, 4, 16, 1, false, "auto", "auto"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
