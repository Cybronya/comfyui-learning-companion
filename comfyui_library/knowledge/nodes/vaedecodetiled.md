# VAEDecodeTiled

## 节点类型

`VAEDecodeTiled`

## 分类

Decoding

## 作用

解码类节点：把编码数据还原（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 17 个 workflow 中。

## 输入

- `samples:LATENT`（18 次）
- `vae:VAE`（18 次）
- `tile_size:INT`（18 次）
- `overlap:INT`（18 次）
- `temporal_size:INT`（18 次）
- `temporal_overlap:INT`（18 次）

## 输出

- `IMAGE:IMAGE`（18 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 64, 64, 8]`（8 次）
- `[512, 128, 4096, 8]`（6 次）
- `[512, 64, 512, 4]`（1 次）
- `[512, 64, 4096, 8]`（1 次）
- `[1024, 64, 1920, 8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
