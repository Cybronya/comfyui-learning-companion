# MiniMaxH3FaceRefinePlanT8Advanced

## 节点类型

`MiniMaxH3FaceRefinePlanT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `frames:IMAGE`（2 次）
- `fps:FLOAT`（2 次）
- `detector_mode:COMBO`（2 次）
- `detector_model:COMBO`（2 次）
- `detector_device:COMBO`（2 次）
- `confidence:FLOAT`（2 次）
- `manual_roi_x:FLOAT`（2 次）
- `manual_roi_y:FLOAT`（2 次）
- `manual_roi_width:FLOAT`（2 次）
- `manual_roi_height:FLOAT`（2 次）

## 输出

- `face_plan:H3_T8_FACE_REFINE_PLAN`（2 次）
- `crops:IMAGE`（2 次）
- `preview:IMAGE`（2 次）
- `report_json:STRING`（2 次）
- `canvas_width:INT`（2 次）
- `canvas_height:INT`（2 次）
- `frame_count:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, "local_opencv_yunet", "facedetection/face_detection_yunet_2023mar.onnx", "cpu", 0.35, 0.3, 0.1, 0.4, 0.55, 0.28, 0.`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
