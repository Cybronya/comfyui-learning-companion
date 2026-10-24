# LayerMask: YoloV8Detect

## 节点类型

`LayerMask: YoloV8Detect`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `image:IMAGE`（10 次）
- `yolo_model:COMBO`（3 次）
- `mask_merge:COMBO`（3 次）
- `conf:FLOAT`（3 次）
- `iou:FLOAT`（3 次）
- `classes:STRING`（3 次）
- `device:STRING`（3 次）
- `max_det:INT`（3 次）
- `retina_masks:BOOLEAN`（3 次）
- `agnostic_nms:BOOLEAN`（3 次）

## 输出

- `mask:MASK`（10 次）
- `yolo_plot_image:IMAGE`（10 次）
- `yolo_masks:MASK`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["face_yolov8m.pt", "all"]`（5 次）
- `["person_yolov8m-seg.pt", "all"]`（2 次）
- `["face_yolov8m.pt", "all", 0.25, 0.45, "", "auto", 300, true, false]`（1 次）
- `["face_yolov9c.pt", "1", 0.25, 0.45, "", "auto", 300, true, false]`（1 次）
- `["yolov8m_seg-speech-bubble.pt", "all", 0.20000000000000004, 0.45, "", "auto", 300, true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
