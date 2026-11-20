# KleinEditComposite

## 节点类型

`KleinEditComposite`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `generated_image:IMAGE`（1 次）
- `original_image:IMAGE`（1 次）
- `custom_mask:MASK`（1 次）
- `delta_e_threshold:FLOAT`（1 次）
- `flow_quality:COMBO`（1 次）
- `use_occlusion:BOOLEAN`（1 次）
- `occlusion_threshold:FLOAT`（1 次）
- `noise_removal_pct:FLOAT`（1 次）
- `close_radius_pct:FLOAT`（1 次）
- `fill_holes:BOOLEAN`（1 次）

## 输出

- `composited_image:IMAGE`（1 次）
- `change_mask:MASK`（1 次）
- `report:STRING`（1 次）
- `debug_gallery:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[-1, "medium", false, -1, 0, 0.5, false, true, 0, 0, 2, 1, false, "replace", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
