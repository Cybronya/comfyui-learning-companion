# Hy3DVAEDecode

## 节点类型

`Hy3DVAEDecode`

## 分类

Decoding

## 作用

解码类节点：把编码数据还原（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `vae:HY3DVAE`（2 次）
- `latents:HY3DLATENT`（2 次）
- `box_v:FLOAT`（2 次）
- `octree_resolution:INT`（2 次）
- `num_chunks:INT`（2 次）
- `mc_level:FLOAT`（2 次）
- `mc_algo:COMBO`（2 次）
- `enable_flash_vdm:BOOLEAN`（2 次）
- `force_offload:BOOLEAN`（2 次）

## 输出

- `trimesh:TRIMESH`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1.01, 384, 32000, 0, "mc", true, true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
