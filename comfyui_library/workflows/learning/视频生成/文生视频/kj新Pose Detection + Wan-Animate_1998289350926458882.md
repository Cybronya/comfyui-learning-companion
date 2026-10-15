---
key: 视频生成/文生视频/kj新Pose Detection + Wan-Animate_1998289350926458882.json
name: kj新Pose Detection + Wan-Animate_1998289350926458882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/kj新Pose Detection + Wan-Animate_1998289350926458882.json
hash: f6bb2ae37b892e81
coverage: 0.613636
learned_at: 2026-10-15 22:47:20
nodes: [SetNode, GetNode, SetNode, easy showAnything, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, ImageResizeKJv2, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), WanVideoModelLoader, WanVideoVAELoader, WanVideoLoraSelectMulti, INTConstant, WanVideoDecode, SetNode, SetNode, GetNode, GetNode, WanVideoSampler, SetNode, easy showAnything, GetImageSize+, easy showAnything, Float, INTConstant, PointsEditor, LoadImage, WanVideoAnimateEmbeds, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoTextEncodeCached, PoseDetectionOneToAllAnimation, PreviewImage, VHS_LoadVideo, INTConstant, INTConstant, SetNode, VHS_VideoCombine, VHS_VideoCombine, OnnxDetectionModelLoader]
patterns: []
missing: []
---

# 视频生成/文生视频/kj新Pose Detection + Wan-Animate_1998289350926458882.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/kj新Pose Detection + Wan-Animate_1998289350926458882.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `SetNode`
- `GetNode`
- `SetNode`
- `easy showAnything`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `WanVideoDecode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `SetNode`
- `easy showAnything`
- `GetImageSize+`
- `easy showAnything`
- `Float`
- `INTConstant`
- `PointsEditor`
- `LoadImage`
- `WanVideoAnimateEmbeds`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
- `VHS_LoadVideo`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`

## 知识

覆盖率 **61%**（27/44）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`INTConstant`、`WanVideoDecode`、`WanVideoSampler`、`GetImageSize+`、`Float`、`PointsEditor`、`LoadImage`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`PoseDetectionOneToAllAnimation`、`VHS_LoadVideo`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
