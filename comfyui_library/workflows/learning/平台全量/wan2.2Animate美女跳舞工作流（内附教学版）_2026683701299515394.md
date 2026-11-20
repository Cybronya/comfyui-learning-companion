---
key: 平台全量/wan2.2Animate美女跳舞工作流（内附教学版）_2026683701299515394.json
name: wan2.2Animate美女跳舞工作流（内附教学版）_2026683701299515394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2Animate美女跳舞工作流（内附教学版）_2026683701299515394.json
hash: 93f3f175b46219a4
coverage: 0.777778
learned_at: 2026-11-14 01:19:34
nodes: [WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetLoRAs, FaceMaskFromPoseKeypoints, ImageResizeKJv2, WanVideoSampler, WanVideoDecode, easy cleanGpuUsed, WanVideoClipVisionEncode, ImageCropByMaskAndResize, PixelPerfectResolution, GetNode, GetNode, GetNode, GetNode, DWPreprocessor, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoVAELoader, CLIPVisionLoader, GetNode, SetNode, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoTextEncodeCached, ImageConcatMulti, ImageConcatMulti, SetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, INTConstant, INTConstant, LoadImage, VHS_LoadVideo, INTConstant]
patterns: []
missing: []
---

# 平台全量/wan2.2Animate美女跳舞工作流（内附教学版）_2026683701299515394.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2Animate美女跳舞工作流（内附教学版）_2026683701299515394.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `FaceMaskFromPoseKeypoints`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoClipVisionEncode`
- `ImageCropByMaskAndResize`
- `PixelPerfectResolution`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `GetNode`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `VHS_LoadVideo`
- `INTConstant`

## 知识

覆盖率 **78%**（28/36）

**有卡**：`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`FaceMaskFromPoseKeypoints`、`ImageResizeKJv2`、`WanVideoSampler`、`WanVideoDecode`、`easy cleanGpuUsed`、`WanVideoClipVisionEncode`、`ImageCropByMaskAndResize`、`PixelPerfectResolution`、`DWPreprocessor`、`WanVideoAnimateEmbeds`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`VHS_VideoCombine`、`INTConstant`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
