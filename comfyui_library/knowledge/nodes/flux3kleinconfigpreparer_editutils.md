# Flux3KleinConfigPreparer_EditUtils

## 节点类型

`Flux3KleinConfigPreparer_EditUtils`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `configs:LIST`（1 次）
- `mask:MASK`（1 次）
- `to_ref:BOOLEAN`（1 次）
- `ref_main_image:BOOLEAN`（1 次）
- `ref_longest_edge:INT`（1 次）
- `ref_crop:COMBO`（1 次）
- `ref_upscale:COMBO`（1 次）
- `pad_mode:COMBO`（1 次）
- `pad_color:COMBO`（1 次）

## 输出

- `configs:LIST`（1 次）
- `config:ANY`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, true, 1024, "pad", "lanczos", "color", "black", "-", 0, "longest_edge", 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
