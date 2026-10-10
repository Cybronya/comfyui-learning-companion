---
key: 视频生成/文生视频/kj新Pose Detection +SteadyDancer_1998291780594491394.json
name: kj新Pose Detection +SteadyDancer_1998291780594491394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/kj新Pose Detection +SteadyDancer_1998291780594491394.json
hash: f8c76b808f350eb9
coverage: 0.878788
learned_at: 2026-10-11 02:57:39
nodes: [WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, PrimitiveNode, WanVideoAddSteadyDancerEmbeds, Note, WanVideoLoraSelect, WanVideoScheduler, PrimitiveNode, WanVideoContextOptions, WanVideoSamplerSettings, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTextEncodeCached, VHS_VideoCombine, WanVideoSamplerFromSettings, OnnxDetectionModelLoader, WanVideoClipVisionEncode, GetImageRangeFromBatch, WanVideoEncode, WanVideoImageToVideoEncode, INTConstant, INTConstant, LoadImage, ImageResizeKJv2, GetImageSizeAndCount, VHS_LoadVideo, PoseDetectionOneToAllAnimation, VHS_VideoCombine, PreviewImage]
patterns: []
missing: []
---

# 视频生成/文生视频/kj新Pose Detection +SteadyDancer_1998291780594491394.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/kj新Pose Detection +SteadyDancer_1998291780594491394.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（33 个）：
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `WanVideoAddSteadyDancerEmbeds`
- `Note`
- `WanVideoLoraSelect`
- `WanVideoScheduler`
- `PrimitiveNode`
- `WanVideoContextOptions`
- `WanVideoSamplerSettings` ★核心
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `WanVideoSamplerFromSettings` ★核心
- `OnnxDetectionModelLoader`
- `WanVideoClipVisionEncode`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `VHS_LoadVideo`
- `PoseDetectionOneToAllAnimation`
- `VHS_VideoCombine`
- `PreviewImage`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoLoraSelect`、`WanVideoScheduler`、`WanVideoContextOptions`、`WanVideoSamplerSettings`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`WanVideoSamplerFromSettings`、`OnnxDetectionModelLoader`、`GetImageRangeFromBatch`、`WanVideoEncode`、`WanVideoImageToVideoEncode`、`INTConstant`、`LoadImage`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`VHS_LoadVideo`、`PoseDetectionOneToAllAnimation`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
