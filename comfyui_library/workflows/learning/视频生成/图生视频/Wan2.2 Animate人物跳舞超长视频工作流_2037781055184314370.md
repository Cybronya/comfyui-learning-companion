---
key: 视频生成/图生视频/Wan2.2 Animate人物跳舞超长视频工作流_2037781055184314370.json
name: Wan2.2 Animate人物跳舞超长视频工作流_2037781055184314370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate人物跳舞超长视频工作流_2037781055184314370.json
hash: 9437a8e986ed7053
coverage: 0.516129
learned_at: 2026-10-15 22:35:58
nodes: [GetNode, GetNode, PreviewImage, SetNode, DrawViTPose, SetNode, SetNode, VHS_VideoCombine, Reroute, easy showAnything, Reroute, ImageFromBatch, PreviewImage, OnnxDetectionModelLoader, SetNode, SetNode, VHS_VideoCombine, PoseAndFaceDetection, GetNode, GetNode, WanVideoLoraSelectMulti, ImageResize+, SetNode, WanVideoDecode, WanVideoModelLoader, VHS_VideoCombine, LoadImage, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, RHHiddenNodes, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate人物跳舞超长视频工作流_2037781055184314370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037781055184314370.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（31 个）：
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
- `ImageResize+`
- `SetNode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RHHiddenNodes`
- `VHS_LoadVideo`

## 知识

覆盖率 **52%**（16/31）

**有卡**：`DrawViTPose`、`VHS_VideoCombine`、`ImageFromBatch`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`WanVideoLoraSelectMulti`、`ImageResize+`、`WanVideoDecode`、`WanVideoModelLoader`、`LoadImage`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`RHHiddenNodes`、`VHS_LoadVideo`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoDecode、WanVideoLoraSelectMulti、ImageResize+、ImageFromBatch、RHHiddenNodes、VHS_LoadVideo
