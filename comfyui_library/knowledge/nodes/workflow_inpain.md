# workflow>INPAIN

## 节点类型

`workflow>INPAIN`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `LayerMask: HumanPartsUltra image:IMAGE`（1 次）
- `LayerMask: SAM2Ultra image:IMAGE`（1 次）
- `destination:MASK`（1 次）
- `InpaintCrop image:IMAGE`（1 次）
- `optional_context_mask:MASK`（1 次）
- `yolo_model:COMBO`（1 次）
- `sort_method:COMBO`（1 次）
- `bbox_select:COMBO`（1 次）
- `select_index:STRING`（1 次）

## 输出

- `preview:IMAGE`（1 次）
- `image:IMAGE`（1 次）
- `LayerMask: SAM2Ultra image:IMAGE`（1 次）
- `stitch:STITCH`（1 次）
- `cropped_image:IMAGE`（1 次）
- `cropped_mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["hand_yolov9c.pt", "left_to_right", "all", "0,", true, true, false, false, false, false, false, false, false, false, fa`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
