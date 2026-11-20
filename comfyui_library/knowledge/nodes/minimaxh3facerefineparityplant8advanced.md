# MiniMaxH3FaceRefineParityPlanT8Advanced

## 节点类型

`MiniMaxH3FaceRefineParityPlanT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `frames:IMAGE`（3 次）
- `fps:FLOAT`（3 次）
- `detector_mode:COMBO`（3 次）
- `detector_model:COMBO`（3 次）
- `detector_device:COMBO`（3 次）
- `confidence:FLOAT`（3 次）
- `manual_roi_x:FLOAT`（3 次）
- `manual_roi_y:FLOAT`（3 次）
- `manual_roi_width:FLOAT`（3 次）
- `manual_roi_height:FLOAT`（3 次）

## 输出

- `face_plan:H3_T8_FACE_REFINE_PARITY_PLAN`（3 次）
- `crops:IMAGE`（3 次）
- `reference_crop:IMAGE`（3 次）
- `preview:IMAGE`（3 次）
- `report_json:STRING`（3 次）
- `canvas_width:INT`（3 次）
- `canvas_height:INT`（3 次）
- `frame_count:INT`（3 次）
- `reference_frame_index:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, "local_ultralytics", "ultralytics/bbox/face_yolov8m.pt", "cpu", 0.35, 0.3, 0.1, 0.4, 0.55, 0.28, 0.18, 4, 21, 51, 2`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
