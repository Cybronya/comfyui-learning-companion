---
key: 数字人/数字人/Wan2.2 Animate人物跳舞超长视频工作流-无劣化_2034828935975931906.json
name: Wan2.2 Animate人物跳舞超长视频工作流-无劣化_2034828935975931906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2 Animate人物跳舞超长视频工作流-无劣化_2034828935975931906.json
hash: 4c7c294a0a06444b
coverage: 0.484848
learned_at: 2026-10-26 01:57:51
nodes: [GetNode, GetNode, PreviewImage, SetNode, DrawViTPose, SetNode, SetNode, VHS_VideoCombine, Reroute, easy showAnything, Reroute, ImageFromBatch, PreviewImage, OnnxDetectionModelLoader, SetNode, SetNode, VHS_VideoCombine, PoseAndFaceDetection, GetNode, GetNode, WanVideoLoraSelectMulti, Note, MarkdownNote, ImageResize+, SetNode, WanVideoDecode, WanVideoModelLoader, VHS_VideoCombine, LoadImage, VHS_LoadVideo, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, RHHiddenNodes]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.2 Animate人物跳舞超长视频工作流-无劣化_2034828935975931906.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2 Animate人物跳舞超长视频工作流-无劣化_2034828935975931906.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（33 个）：
- `GetNode`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `DrawViTPose`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `Reroute`
- `easy showAnything`
- `Reroute`
- `ImageFromBatch`
- `PreviewImage`
- `OnnxDetectionModelLoader`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `Note`
- `MarkdownNote`
- `ImageResize+`
- `SetNode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RHHiddenNodes`

## 知识

覆盖率 **48%**（16/33）

**有卡**：`DrawViTPose`、`VHS_VideoCombine`、`ImageFromBatch`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`WanVideoLoraSelectMulti`、`ImageResize+`、`WanVideoDecode`、`WanVideoModelLoader`、`LoadImage`、`VHS_LoadVideo`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`RHHiddenNodes`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoDecode、WanVideoLoraSelectMulti、ImageResize+、ImageFromBatch、RHHiddenNodes、VHS_LoadVideo
