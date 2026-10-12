# FaceAlignmentCropper

## 节点类型

`FaceAlignmentCropper`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `face_detector:COMBO`（1 次）
- `landmarkrunner_device:COMBO`（1 次）
- `face_detector_device:COMBO`（1 次）
- `face_detector_dtype:COMBO`（1 次）
- `keep_model_loaded:BOOLEAN`（1 次）

## 输出

- `cropper:FSMCROPPER`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["blazeface_back_camera", "torch_gpu", "cuda", "fp16", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
