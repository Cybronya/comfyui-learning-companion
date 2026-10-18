---
key: 视频生成/图生视频/WAN2.2Animate美女图片跳舞工作流【动作，表情迁移】_1971382412112510978.json
name: WAN2.2Animate美女图片跳舞工作流【动作，表情迁移】_1971382412112510978.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2Animate美女图片跳舞工作流【动作，表情迁移】_1971382412112510978.json
hash: 527c28976706aeec
coverage: 0.695652
learned_at: 2026-10-15 22:31:56
nodes: [WanVideoSampler, WanVideoDecode, easy cleanGpuUsed, JWInteger, CLIPVisionLoader, LayerUtility: PurgeVRAM, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoBlockSwap, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VHS_VideoInfo, PixelPerfectResolution, SetNode, SetNode, FaceMaskFromPoseKeypoints, LayerUtility: PurgeVRAM, GetNode, GetNode, GetNode, DWPreprocessor, GetNode, VHS_VideoCombine, SetNode, SetNode, SetNode, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, ImageResizeKJv2, Text, ImageCropByMaskAndResize, JWInteger, WanVideoTextEncodeCached, SetNode, ImageConcatMulti, LoadImage, VHS_LoadVideo, GetNode, GetNode, VHS_VideoCombine, GetNode, SetNode, ImageConcatMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2Animate美女图片跳舞工作流【动作，表情迁移】_1971382412112510978.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971382412112510978.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（46 个）：
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `JWInteger`
- `CLIPVisionLoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoInfo`
- `PixelPerfectResolution`
- `SetNode`
- `SetNode`
- `FaceMaskFromPoseKeypoints`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `ImageResizeKJv2`
- `Text`
- `ImageCropByMaskAndResize`
- `JWInteger`
- `WanVideoTextEncodeCached`
- `SetNode`
- `ImageConcatMulti`
- `LoadImage`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`

## 知识

覆盖率 **70%**（32/46）

**有卡**：`WanVideoSampler`、`WanVideoDecode`、`easy cleanGpuUsed`、`JWInteger`、`CLIPVisionLoader`、`LayerUtility: PurgeVRAM`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`VHS_VideoInfo`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`ImageResizeKJv2`、`Text`、`ImageCropByMaskAndResize`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
