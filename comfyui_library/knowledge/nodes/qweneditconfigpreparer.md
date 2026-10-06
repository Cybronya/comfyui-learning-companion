# QwenEditConfigPreparer

## 节点类型

`QwenEditConfigPreparer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `image:IMAGE`（9 次）
- `configs:LIST`（9 次）
- `mask:MASK`（9 次）
- `to_ref:BOOLEAN`（9 次）
- `ref_main_image:BOOLEAN`（9 次）
- `ref_longest_edge:INT`（9 次）
- `ref_crop:COMBO`（9 次）
- `ref_upscale:COMBO`（9 次）
- `to_vl:BOOLEAN`（9 次）
- `vl_resize:BOOLEAN`（9 次）

## 输出

- `configs:LIST`（9 次）
- `config:ANY`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, true, 1024, "pad", "lanczos", true, true, 384, "center", "lanczos"]`（3 次）
- `[true, false, 1536, "pad", "lanczos", true, true, 384, "center", "bicubic"]`（3 次）
- `[true, true, 1536, "pad", "lanczos", true, true, 384, "center", "bicubic"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
