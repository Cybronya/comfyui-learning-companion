# RMBG

## 节点类型

`RMBG`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `model:COMBO`（3 次）
- `sensitivity:FLOAT`（3 次）
- `process_res:INT`（3 次）
- `mask_blur:INT`（3 次）
- `mask_offset:INT`（3 次）
- `invert_output:BOOLEAN`（3 次）
- `refine_foreground:BOOLEAN`（3 次）
- `background:COMBO`（3 次）
- `background_color:COLORCODE`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）
- `MASK:MASK`（3 次）
- `MASK_IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["RMBG-2.0", 1, 1024, 0, 0, false, false, "Color", "#ffffff"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
