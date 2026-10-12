# FaceHandCrop

## 节点类型

`FaceHandCrop`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `model_path:COMBO`（1 次）
- `max_faces:INT`（1 次）
- `start_face:INT`（1 次）
- `padding_ratio:FLOAT`（1 次）
- `maskpadding_ratio:FLOAT`（1 次）
- `face_position:FLOAT`（1 次）
- `enable_resize:BOOLEAN`（1 次）
- `target_width:INT`（1 次）

## 输出

- `cropped_image:IMAGE`（1 次）
- `face_mask:MASK`（1 次）
- `crop_mask_full:MASK`（1 次）
- `crop_info:CROP_INFO`（1 次）
- `face_count:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["face_yolov8m.pt", 3, 1, 1.8, 1.8, 0.62, true, 1280, 1024, "white", 16]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
