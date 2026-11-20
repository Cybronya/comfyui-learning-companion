# Trellis2DecodeLatents

## 节点类型

`Trellis2DecodeLatents`

## 分类

Decoding

## 作用

解码类节点：把编码数据还原（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:TRELLIS2PIPELINE`（1 次）
- `shape_slat:SHAPE_SLAT`（1 次）
- `texture_slat:TEXTURE_SLAT`（1 次）
- `resolution:INT`（1 次）
- `use_tiled_decoder:BOOLEAN`（1 次）

## 输出

- `mesh:MESHWITHVOXEL`（1 次）
- `bvh:BVH`（1 次）
- `pipeline:TRELLIS2PIPELINE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
