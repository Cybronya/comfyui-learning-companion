# Flux2KleinConfigPreparer_EditUtils

## 节点类型

`Flux2KleinConfigPreparer_EditUtils`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `image:IMAGE`（9 次）
- `configs:LIST`（9 次）
- `mask:MASK`（9 次）
- `to_ref:BOOLEAN`（9 次）
- `ref_main_image:BOOLEAN`（9 次）
- `ref_longest_edge:INT`（9 次）
- `ref_crop:COMBO`（9 次）
- `ref_upscale:COMBO`（9 次）
- `ref_resize_mode:COMBO`（9 次）
- `rope_x_offset:INT`（9 次）

## 输出

- `configs:LIST`（9 次）
- `config:ANY`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, true, 1024, "pad", "lanczos", "color", "black", "-", 0, "longest_edge", 0, 0]`（7 次）
- `[true, true, 1024, "pad", "lanczos", "longest_edge", 0, 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
