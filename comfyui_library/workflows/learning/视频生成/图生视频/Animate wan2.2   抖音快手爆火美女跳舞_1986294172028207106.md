---
key: 视频生成/图生视频/Animate wan2.2   抖音快手爆火美女跳舞_1986294172028207106.json
name: Animate wan2.2   抖音快手爆火美女跳舞_1986294172028207106.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Animate wan2.2   抖音快手爆火美女跳舞_1986294172028207106.json
hash: 6958ca3702b4a8b5
coverage: 0.809524
learned_at: 2026-10-15 22:32:54
nodes: [SimpleMath+, SetNode, GetNode, GetNode, GetNode, SetNode, VHS_VideoCombine, VHS_LoadVideo, LoadImage, Note, JWInteger, JWInteger, PrimitiveInt, ttN float, ttN float, ttN float, WanVideoModelLoader, WanVideoLoraSelectMulti, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoBlockSwap, ImageCropByMaskAndResize, DWPreprocessor, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoClipVisionEncode, VHS_VideoInfo, WanVideoTextEncodeCached, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, easy cleanGpuUsed, SetNode, FaceMaskFromPoseKeypoints, WanVideoVAELoader, CLIPVisionLoader, PixelPerfectResolution, CLIPVisionLoader, ImageResizeKJv2, WanVideoClipVisionEncode, WanVideoDecode, WanVideoSampler, WanVideoAnimateEmbeds]
patterns: []
missing: []
---

# 视频生成/图生视频/Animate wan2.2   抖音快手爆火美女跳舞_1986294172028207106.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1986294172028207106.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
- `SimpleMath+`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `Note`
- `JWInteger`
- `JWInteger`
- `PrimitiveInt`
- `ttN float`
- `ttN float`
- `ttN float`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoBlockSwap`
- `ImageCropByMaskAndResize`
- `DWPreprocessor`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoClipVisionEncode`
- `VHS_VideoInfo`
- `WanVideoTextEncodeCached`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `SetNode`
- `FaceMaskFromPoseKeypoints`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `PixelPerfectResolution`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`

## 知识

覆盖率 **81%**（34/42）

**有卡**：`SimpleMath+`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`、`JWInteger`、`ttN float`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`LayerUtility: PurgeVRAM`、`WanVideoBlockSwap`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoClipVisionEncode`、`VHS_VideoInfo`、`WanVideoTextEncodeCached`、`easy cleanGpuUsed`、`FaceMaskFromPoseKeypoints`、`WanVideoVAELoader`、`CLIPVisionLoader`、`PixelPerfectResolution`、`ImageResizeKJv2`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoAnimateEmbeds`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
