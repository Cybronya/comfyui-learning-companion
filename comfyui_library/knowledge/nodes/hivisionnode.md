# HivisionNode

## 节点类型

`HivisionNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `input_img:IMAGE`（2 次）
- `normal_params:PARAMS`（2 次）
- `face_alignment:BOOLEAN`（2 次）
- `change_bg_only:BOOLEAN`（2 次）
- `crop_only:BOOLEAN`（2 次）
- `matting_model:COMBO`（2 次）
- `face_detect_model:COMBO`（2 次）
- `head_measure_ratio:FLOAT`（2 次）
- `top_distance:FLOAT`（2 次）
- `whitening_strength:INT`（2 次）

## 输出

- `standard_img:IMAGE`（2 次）
- `hd_img:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, false, false, "modnet_photographic_portrait_matting", "mtcnn", 0.2, 0.12, 1, 0, 0, 0, 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
