# LayerUtility: GetColorToneV2

## 节点类型

`LayerUtility: GetColorToneV2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `mask:MASK`（4 次）
- `mode:COMBO`（1 次）
- `color_of:COMBO`（1 次）
- `remove_bkgd_method:COMBO`（1 次）
- `invert_mask:BOOLEAN`（1 次）
- `mask_grow:INT`（1 次）

## 输出

- `image:IMAGE`（4 次）
- `color_in_hex:STRING`（4 次）
- `HSV color in list:LIST`（4 次）
- `mask:MASK`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["average", "subject", "BiRefNet", false, 16]`（2 次）
- `["average", "mask", "none", false, 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
