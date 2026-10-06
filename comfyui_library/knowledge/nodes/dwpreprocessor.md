# DWPreprocessor

## 节点类型

`DWPreprocessor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `detect_hand:COMBO`（4 次）
- `detect_body:COMBO`（4 次）
- `detect_face:COMBO`（4 次）
- `resolution:INT`（4 次）
- `bbox_detector:COMBO`（4 次）
- `pose_estimator:COMBO`（4 次）
- `scale_stick_for_xinsr_cn:COMBO`（4 次）

## 输出

- `IMAGE:IMAGE`（4 次）
- `POSE_KEYPOINT:POSE_KEYPOINT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["enable", "enable", "enable", 1024, "yolox_l.torchscript.pt", "dw-ll_ucoco_384_bs5.torchscript.pt", "disable"]`（3 次）
- `["enable", "enable", "enable", 1024, "yolox_l.onnx", "dw-ll_ucoco_384_bs5.torchscript.pt", "disable"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
