# FaceAutoFitDouble

## 节点类型

`FaceAutoFitDouble`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_L:IMAGE`（1 次）
- `mask_L:MASK`（1 次）
- `image_R:IMAGE`（1 次）
- `mask_R:MASK`（1 次）
- `mode:COMBO`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask_L:MASK`（1 次）
- `mask_R:MASK`（1 次）
- `mask_combined:MASK`（1 次）
- `gender_L:INT`（1 次）
- `gender_R:INT`（1 次）
- `mode_code:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["half_body", "white", 0, -0.29890677847522795, 0.8042304934973004, 2.458936401456043, 0.9500000000000002, 1.00000000000`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
