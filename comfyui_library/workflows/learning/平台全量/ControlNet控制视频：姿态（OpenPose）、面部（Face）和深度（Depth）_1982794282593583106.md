---
key: 平台全量/ControlNet控制视频：姿态（OpenPose）、面部（Face）和深度（Depth）_1982794282593583106.json
name: ControlNet控制视频：姿态（OpenPose）、面部（Face）和深度（Depth）_1982794282593583106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ControlNet控制视频：姿态（OpenPose）、面部（Face）和深度（Depth）_1982794282593583106.json
hash: 9dd5cdb0ddbcd27d
coverage: 0.95
learned_at: 2026-11-14 00:22:55
nodes: [ControlNetLoader, DepthAnythingV2Preprocessor, SetUnionControlNetType, ImageResizeKJv2, Fast Groups Muter (rgthree), VHS_VideoInfo, VHS_LoadVideo, RMBG, VHS_VideoCombine, OnnxDetectionModelLoader, PixelPerfectResolution, GetImageSizeAndCount, PoseAndFaceDetection, VHS_VideoCombine, DrawViTPose, DWPreprocessor, LayerUtility: ImageBlend, VHS_VideoCombine, easy int, easy int]
patterns: []
missing: []
---

# 平台全量/ControlNet控制视频：姿态（OpenPose）、面部（Face）和深度（Depth）_1982794282593583106.json

> 来源文件 `comfyui_library/workflows/平台全量/ControlNet控制视频：姿态（OpenPose）、面部（Face）和深度（Depth）_1982794282593583106.json`

## 结构

**生成流程**：Model → Control → Process → Other

**节点**（20 个）：
- `ControlNetLoader`
- `DepthAnythingV2Preprocessor`
- `SetUnionControlNetType`
- `ImageResizeKJv2`
- `Fast Groups Muter (rgthree)`
- `VHS_VideoInfo`
- `VHS_LoadVideo`
- `RMBG`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `PixelPerfectResolution`
- `GetImageSizeAndCount`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `DrawViTPose`
- `DWPreprocessor`
- `LayerUtility: ImageBlend`
- `VHS_VideoCombine`
- `easy int`
- `easy int`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`ControlNetLoader`、`DepthAnythingV2Preprocessor`、`SetUnionControlNetType`、`ImageResizeKJv2`、`VHS_VideoInfo`、`VHS_LoadVideo`、`RMBG`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`PixelPerfectResolution`、`GetImageSizeAndCount`、`PoseAndFaceDetection`、`DrawViTPose`、`DWPreprocessor`、`LayerUtility: ImageBlend`、`easy int`

**用到的条目**：ControlNetLoader、DepthAnythingV2Preprocessor、SetUnionControlNetType、GetImageSizeAndCount、ImageResizeKJv2、PixelPerfectResolution、DrawViTPose、DWPreprocessor
