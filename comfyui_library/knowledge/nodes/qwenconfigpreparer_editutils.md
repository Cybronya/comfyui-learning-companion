# QwenConfigPreparer_EditUtils

## 节点类型

`QwenConfigPreparer_EditUtils`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `configs:LIST`（2 次）
- `mask:MASK`（2 次）
- `to_ref:BOOLEAN`（2 次）
- `ref_main_image:BOOLEAN`（2 次）
- `ref_longest_edge:INT`（2 次）
- `ref_crop:COMBO`（2 次）
- `ref_upscale:COMBO`（2 次）
- `to_vl:BOOLEAN`（2 次）
- `vl_resize:BOOLEAN`（2 次）

## 输出

- `configs:LIST`（2 次）
- `config:ANY`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, true, 1920, "pad", "lanczos", true, true, 384, "center", "lanczos", "longest_edge"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
