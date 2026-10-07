# VaeDecodeShapeTrellis

## 节点类型

`VaeDecodeShapeTrellis`

## 分类

Decoding

## 作用

解码类节点：把编码数据还原（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `samples:LATENT`（2 次）
- `vae:VAE`（2 次）

## 输出

- `mesh:MESH`（2 次）
- `shape_subdivides:SHAPE_SUBDIVIDES`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
