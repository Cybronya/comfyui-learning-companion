# VAEUtils_VAEDecodeTiled

## 节点类型

`VAEUtils_VAEDecodeTiled`

## 分类

Decoding

## 作用

解码类节点：把编码数据还原（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `samples:LATENT`（1 次）
- `vae:VAE`（1 次）
- `upscale:INT`（1 次）
- `tile:BOOLEAN`（1 次）
- `tile_size:INT`（1 次）
- `overlap:INT`（1 次）
- `temporal_size:INT`（1 次）
- `temporal_overlap:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[-1, false, 512, 64, 4096, 64]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
