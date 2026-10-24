# SAM3DBodyProcess

## 节点类型

`SAM3DBodyProcess`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:SAM3D_MODEL`（1 次）
- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `bbox_threshold:FLOAT`（1 次）
- `inference_type:COMBO`（1 次）
- `use_detector:BOOLEAN`（1 次）
- `use_segmentor:BOOLEAN`（1 次）
- `use_fov_estimator:BOOLEAN`（1 次）

## 输出

- `mesh_data:SAM3D_OUTPUT`（1 次）
- `skeleton:SKELETON`（1 次）
- `debug_image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.8, "full", false, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
