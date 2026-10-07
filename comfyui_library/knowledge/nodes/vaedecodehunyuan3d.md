# VAEDecodeHunyuan3D

## 节点类型

`VAEDecodeHunyuan3D`

## 分类

Decoding

## 作用

解码类节点：把编码数据还原（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `samples:LATENT`（4 次）
- `vae:VAE`（4 次）

## 输出

- `VOXEL:VOXEL`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[8000, 256]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
