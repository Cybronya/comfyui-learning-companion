# QwenImage21ConfigPreparer_EditUtils

## 节点类型

`QwenImage21ConfigPreparer_EditUtils`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（10 次）
- `configs:LIST`（10 次）
- `mask:MASK`（10 次）
- `to_ref:BOOLEAN`（10 次）
- `ref_main_image:BOOLEAN`（10 次）
- `ref_longest_edge:INT`（10 次）
- `ref_crop:COMBO`（10 次）
- `ref_upscale:COMBO`（10 次）
- `to_vl:BOOLEAN`（10 次）
- `ref_resize_mode:COMBO`（10 次）

## 输出

- `configs:LIST`（10 次）
- `config:ANY`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, true, 1376, "pad", "lanczos", true, "longest_edge", 0, 0, "color", "white", "-", 0]`（6 次）
- `[true, false, 1024, "pad", "lanczos", true, "longest_edge", 0, 0, "color", "white", "-", 0]`（2 次）
- `[true, true, 1024, "pad", "lanczos", true, "longest_edge", 0, 0, "color", "white", "-", 0]`（1 次）
- `[true, true, 1536, "pad", "lanczos", true, "longest_edge", 0, 0, "color", "white", "-", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
