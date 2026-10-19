# DepthAnything_V3

## 节点类型

`DepthAnything_V3`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `da3_model:DA3MODEL`（2 次）
- `images:IMAGE`（2 次）
- `camera_params:CAMERA_PARAMS`（2 次）
- `normalization_mode:COMBO`（1 次）
- `resize_method:COMBO`（1 次）
- `invert_depth:BOOLEAN`（1 次）
- `keep_model_size:BOOLEAN`（1 次）

## 输出

- `depth:IMAGE`（2 次）
- `confidence:IMAGE`（1 次）
- `resized_rgb_image:IMAGE`（1 次）
- `ray_origin:IMAGE`（1 次）
- `ray_direction:IMAGE`（1 次）
- `extrinsics:STRING`（1 次）
- `intrinsics:STRING`（1 次）
- `sky_mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[]`（1 次）
- `["V2-Style", "resize", false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
