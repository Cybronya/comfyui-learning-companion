# SDMatteApply

## 节点类型

`SDMatteApply`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `trimap:MASK`（1 次）
- `model_name:COMBO`（1 次）
- `inference_size:COMBO`（1 次）
- `is_transparent:BOOLEAN`（1 次）
- `output_mode:COMBO`（1 次）
- `mask_refine:BOOLEAN`（1 次）
- `trimap_constraint:FLOAT`（1 次）
- `force_cpu:BOOLEAN`（1 次）

## 输出

- `alpha_mask:MASK`（1 次）
- `matted_image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["SDMatte_plus.pth", 1024, false, "matted_rgb", true, 0.8, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
