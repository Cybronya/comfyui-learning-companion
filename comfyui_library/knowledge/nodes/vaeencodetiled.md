# VAEEncodeTiled

## 节点类型

`VAEEncodeTiled`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `pixels:IMAGE`（7 次）
- `vae:VAE`（7 次）
- `tile_size:INT`（7 次）
- `overlap:INT`（7 次）
- `temporal_size:INT`（7 次）
- `temporal_overlap:INT`（7 次）

## 输出

- `LATENT:LATENT`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 128, 4096, 8]`（6 次）
- `[1024, 64, 1920, 8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
