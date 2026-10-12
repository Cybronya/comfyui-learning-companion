# ReActorMaskHelper

## 节点类型

`ReActorMaskHelper`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `swapped_image:IMAGE`（2 次）
- `mask_optional:MASK`（2 次）
- `bbox_model_name:COMBO`（2 次）
- `bbox_threshold:FLOAT`（2 次）
- `bbox_dilation:INT`（2 次）
- `bbox_crop_factor:FLOAT`（2 次）
- `bbox_drop_size:INT`（2 次）
- `sam_model_name:COMBO`（2 次）
- `sam_dilation:INT`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `MASK:MASK`（2 次）
- `MASK_PREVIEW:IMAGE`（2 次）
- `SWAPPED_FACE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["bbox/face_yolov8m.pt", 0.5, 10, 3, 10, "sam_vit_b_01ec64.pth", 0, 0.93, 0, 0.7, "False", "dilate", 0, 9, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
