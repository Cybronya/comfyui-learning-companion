# ReinhardColorTransfer

## 节点类型

`ReinhardColorTransfer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `reference:IMAGE`（1 次）
- `ref_mask:MASK`（1 次）
- `output_mask:MASK`（1 次）
- `mode:COMBO`（1 次）
- `strength:FLOAT`（1 次）
- `use_tile_processing:BOOLEAN`（1 次）
- `tile_size:INT`（1 次）
- `padding:INT`（1 次）
- `mask_feather:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["chroma_only", 0.8500000000000002, true, 512, 64, 20]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
