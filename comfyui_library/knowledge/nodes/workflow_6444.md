# workflow>物体检测

## 节点类型

`workflow>物体检测`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `LayerMask: ObjectDetectorYOLO8 image:IMAGE`（1 次）
- `image:IMAGE`（1 次）
- `LayerMask: DrawBBoxMaskV2 image:IMAGE`（1 次）
- `mask_c:MASK`（1 次）
- `mask_d:MASK`（1 次）
- `mask_e:MASK`（1 次）
- `mask_f:MASK`（1 次）
- `yolo_model:COMBO`（1 次）
- `sort_method:COMBO`（1 次）

## 输出

- `预览图像:IMAGE`（1 次）
- `LayerMask: ObjectDetectorYOLO8 预览图像:IMAGE`（1 次）
- `MASK:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["head_yolov8n.pt", "big_to_small", "first", "0,", "face_yolov8m.pt", "big_to_small", "first", "0,", 0, -0.3000000000000`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
