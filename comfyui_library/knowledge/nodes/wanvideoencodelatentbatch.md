# WanVideoEncodeLatentBatch

## 节点类型

`WanVideoEncodeLatentBatch`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vae:WANVAE`（1 次）
- `images:IMAGE`（1 次）
- `enable_vae_tiling:BOOLEAN`（1 次）
- `tile_x:INT`（1 次）
- `tile_y:INT`（1 次）
- `tile_stride_x:INT`（1 次）
- `tile_stride_y:INT`（1 次）

## 输出

- `samples:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, 272, 272, 144, 128]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
