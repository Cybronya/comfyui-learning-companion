---
key: 视频生成/图生视频/视频二创人物 背景完美高清替换Wan Animate+SeedVR2.5_1996912831717130242.json
name: 视频二创人物 背景完美高清替换Wan Animate+SeedVR2.5_1996912831717130242.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1996912831717130242.json
hash: 6929ec9113cc7a2d
coverage: 0.964286
learned_at: 2026-10-15 22:33:28
nodes: [WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, SDPoseOODLoader, SDPoseOODProcessor, OnnxDetectionModelLoader, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, PoseAndFaceDetection, WanVideoSampler, WanVideoAnimateEmbeds, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, ImageResizeKJv2, ImageResizeKJv2, FlashVSRNode, WanVideoDecode, LayerUtility: PurgeVRAM V2, Int, Int, RHHiddenNodes, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/视频二创人物 背景完美高清替换Wan Animate+SeedVR2.5_1996912831717130242.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1996912831717130242.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `OnnxDetectionModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `FlashVSRNode`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `Int`
- `Int`
- `RHHiddenNodes`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`SDPoseOODLoader`、`SDPoseOODProcessor`、`OnnxDetectionModelLoader`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`VHS_VideoCombine`、`VHS_LoadVideo`、`ImageResizeKJv2`、`FlashVSRNode`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`Int`、`RHHiddenNodes`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、CLIPVisionLoader
