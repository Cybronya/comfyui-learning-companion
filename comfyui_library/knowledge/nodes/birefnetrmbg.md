# BiRefNetRMBG

## 节点类型

`BiRefNetRMBG`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `model:COMBO`（2 次）
- `mask_blur:INT`（2 次）
- `mask_offset:INT`（2 次）
- `invert_output:BOOLEAN`（2 次）
- `refine_foreground:BOOLEAN`（2 次）
- `background:COMBO`（2 次）
- `background_color:COLORCODE`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `MASK:MASK`（2 次）
- `MASK_IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["BiRefNet-portrait", 0, 0, false, false, "Color", "#ffffff"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
