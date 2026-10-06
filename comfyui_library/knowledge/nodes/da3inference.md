# DA3Inference

## 节点类型

`DA3Inference`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `da3_model:DA3_MODEL`（2 次）
- `image:IMAGE`（2 次）
- `resolution:INT`（2 次）
- `resize_method:COMBO`（2 次）
- `mode:COMFY_DYNAMICCOMBO_V3`（2 次）
- `mode.ref_view_strategy:COMBO`（2 次）
- `mode.pose_method:COMBO`（2 次）

## 输出

- `da3_geometry:DA3_GEOMETRY`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[504, "upper_bound_resize", "multiview", "saddle_balanced", "cam_dec"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
